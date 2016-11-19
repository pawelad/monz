# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click
import dateutil.parser
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
            fg='green'
        )

        click.echo("\t{0:<8} {1}".format('id', account['id']))
        click.echo("\t{0:<8} {1:%b %-d, %Y %-I:%M %p}".format(
            'created', dateutil.parser.parse(account['created']))
        )

        if n != len(monzo_accounts):
            click.echo()  # Print new line between accounts


if __name__ == '__main__':
    cli(obj={})
