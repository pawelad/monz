# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from decimal import Decimal

import click
import dateutil.parser
from babel.numbers import format_currency
from pymonzo import MonzoAPI


@click.group()
@click.option('--access-token', '-t', type=str, help="Monzo API access token.")
@click.pass_context
def cli(ctx, access_token):
    try:
        ctx.obj['monzo_api'] = MonzoAPI(access_token=access_token)
    except ValueError as e:
        raise click.ClickException(e)


@cli.command()
@click.pass_context
def accounts(ctx):
    """Show connected Monzo accounts"""
    monzo_accounts = ctx.obj['monzo_api'].accounts()

    for n, account in enumerate(monzo_accounts, start=1):
        click.secho(
            "Account #{}, {}".format(n, account['description']),
            fg='green',
        )

        click.echo('{0:<12} {1}'.format('ID:', account['id']))
        click.echo('{0:<12} {1:%b %-d, %Y %-I:%M %p}'.format(
            'Created:', dateutil.parser.parse(account['created']))
        )

        if n != len(monzo_accounts):
            click.echo()  # Print new line between accounts


@cli.command()
@click.option('--account-id', '-a', type=str, help="Monzo account ID.")
@click.pass_context
def balance(ctx, account_id):
    """Show Monzo account balance"""
    try:
        monzo_balance = ctx.obj['monzo_api'].balance(account_id=account_id)
    except ValueError as e:
        raise click.ClickException(e)

    # API returns balance without the delimiter before the subunit,
    # so 12345 is in fact 123.45
    value = Decimal(
        str(monzo_balance['balance'])[:-2] + '.' +
        str(monzo_balance['balance'])[-2:]
    )
    local_value = format_currency(value, monzo_balance['currency'])
    local_spent_today = format_currency(
        monzo_balance['spend_today'], monzo_balance['currency']
    )

    click.secho('{0:<12} {1}'.format('Balance:', local_value), fg='green')
    click.echo('{0:<12} {1}'.format('Spent today:', local_spent_today))


if __name__ == '__main__':
    cli(obj={})
