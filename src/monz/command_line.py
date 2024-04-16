"""monz command line interface."""

from datetime import datetime, timedelta
from typing import List, Optional

import click
import rich_click
from pymonzo import MonzoAPI
from pymonzo.exceptions import PyMonzoError
from pymonzo.transactions import MonzoTransaction
from rich.console import Console

from monz.utils import DefaultRichGroup

help_config = rich_click.RichHelpConfiguration(
    max_width=88,
    use_markdown=True,
)

rich_console = Console()

# Options used in multiple places
option_account_id = click.option(
    "--account_id",
    "-a",
    type=str,
    help="Monzo account ID. Can be omitted if user has only one (active) account.",
)


@click.group(cls=DefaultRichGroup, default="info", default_if_no_args=True)
@rich_click.rich_config(help_config=help_config)
@click.version_option()
@click.option("--access_token", "-t", type=str, help="OAuth access token.")
@click.pass_context
def cli(ctx: click.Context, access_token: Optional[str]) -> None:
    """Simple command line interface for quickly accessing your Monzo account info.

    To use it, you need to first authenticate the app. You can do that with a temporary
    access token from the [Monzo Developer Portal](https://developers.monzo.com/),
    or go through a one time OAuth setup that will save the token on disk and
    automatically refresh it when it expires.

    To do that, you should first create an OAuth client in Monzo developer tools
    (with the "Redirect URL" set to `http://localhost:6600/monz`) and run the
    `monz authorize` command with obtained client ID and client secret.

    For more information, please take a look at:
    https://monz.pawelad.dev/en/latest/getting_started/#authentication
    """
    if ctx.invoked_subcommand != "authorize":
        try:
            ctx.obj = MonzoAPI(access_token=access_token)
        except PyMonzoError as e:
            raise click.UsageError(str(e)) from e


@cli.command()
@click.option(
    "--client_id",
    type=str,
    required=True,
    prompt="Monzo OAuth client ID",
    help="Monzo OAuth client ID.",
)
@click.option(
    "--client_secret",
    type=str,
    required=True,
    prompt="Monzo OAuth client secret",
    hide_input=True,
    help="Monzo OAuth client secret.",
)
@click.option(
    "--save/--no_save",
    default=True,
    help="Whether to save the token to disk.",
)
@click.option(
    "--redirect_url",
    type=str,
    default="http://localhost:6600/monz",
    help="Redirect URL specified in OAuth client.",
)
def authorize(
    client_id: str,
    client_secret: str,
    save: bool,
    redirect_url: str,
) -> None:
    """Authorize `monz` as an OAuth client.

    To get the client ID and secret, create an OAuth client in
    [Monzo developer tools](https://developers.monzo.com/) (with the "Redirect URL"
    set to `http://localhost:6600/monz`), run the `monz authorize` command and follow
    its steps. By default, it will save the obtained token on disk, so it can be
    automatically refreshed when it expires.

    Alternatively, you can pass `--no_save` option to just obtain the token.
    """
    token = MonzoAPI.authorize(
        client_id=client_id,
        client_secret=client_secret,
        save_to_disk=save,
        redirect_uri=redirect_url,
    )

    if not save:
        rich_console.print_json(data=token)


@cli.command()
@click.pass_context
def info(ctx: click.Context) -> None:
    """Show Monzo account overview."""
    ctx.invoke(balance)

    rich_console.print()

    rich_console.print("[bold magenta]Last transaction:")
    ctx.invoke(transactions, num=1)


@cli.command()
@click.pass_obj
def whoami(monzo_api: MonzoAPI) -> None:
    """Show Monzo `whoami` data."""
    try:
        monzo_whoami = monzo_api.whoami()
    except PyMonzoError as e:
        raise click.UsageError(str(e)) from e

    rich_console.print(monzo_whoami)


@cli.command()
@click.pass_obj
def accounts(monzo_api: MonzoAPI) -> None:
    """Show Monzo accounts."""
    try:
        monzo_accounts = monzo_api.accounts.list()
    except PyMonzoError as e:
        raise click.UsageError(str(e)) from e

    for n, account in enumerate(monzo_accounts, start=1):
        rich_console.print(account)

        # Print a new line between accounts
        if n != len(monzo_accounts):
            rich_console.print()


@cli.command()
@option_account_id
@click.pass_obj
def balance(monzo_api: MonzoAPI, account_id: Optional[str]) -> None:
    """Show Monzo account balance.

    You don't need to specify the account ID if you only have one (active) account.
    """
    try:
        monzo_balance = monzo_api.balance.get(account_id=account_id)
    except PyMonzoError as e:
        raise click.UsageError(str(e)) from e

    rich_console.print(monzo_balance)


@cli.command()
@option_account_id
@click.option(
    "--show_deleted/--hide_deleted",
    default=False,
    help="Whether to show deleted pots.",
)
@click.pass_obj
def pots(monzo_api: MonzoAPI, account_id: Optional[str], show_deleted: bool) -> None:
    """Show Monzo pots."""
    try:
        monzo_pots = monzo_api.pots.list(account_id=account_id)
    except PyMonzoError as e:
        raise click.UsageError(str(e)) from e

    if not show_deleted:
        monzo_pots = [pot for pot in monzo_pots if not pot.deleted]

    for n, pot in enumerate(monzo_pots, start=1):
        rich_console.print(pot)

        # Print a new line between accounts
        if n != len(monzo_pots):
            rich_console.print()


@cli.command()
@option_account_id
@click.option(
    "--num",
    "-n",
    type=int,
    default=3,
    help="Number of transactions to show.",
)
@click.pass_obj
def transactions(monzo_api: MonzoAPI, account_id: Optional[str], num: int) -> None:
    """Show Monzo account transactions.

    You don't need to specify the account ID if you only have one (active) account.

    Per [Monzo API docs] - you can only fetch all transactions within 5 minutes of
    authentication. After that, you can query your last 90 days.

    [Monzo API docs]: https://docs.monzo.com/#list-transactions
    """
    try:
        # By default, the API returns transactions from the last 30 days (I think).
        # Because of that, query the api with an increasing `since` parameter until we
        # get the desired number of transactions.
        monzo_transactions: List[MonzoTransaction] = []
        n = 0
        while len(monzo_transactions) < num:
            n += 1
            since = datetime.today() - timedelta(days=30 * n)
            monzo_transactions = monzo_api.transactions.list(
                account_id=account_id,
                expand_merchant=True,
                since=since,
            )
    except PyMonzoError as e:
        raise click.UsageError(str(e)) from e

    for n, transaction in enumerate(list(reversed(monzo_transactions))[:num], start=1):
        rich_console.print(transaction)

        # Print a new line between transactions
        if n != len(monzo_transactions):
            rich_console.print()
