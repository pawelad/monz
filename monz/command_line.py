# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click
from pymonzo import MonzoAPI


@click.command()
@click.option('--access-token', '-t', type=str, help="Monzo API access token")
def cli(access_token):
    try:
        monzo_api = MonzoAPI(access_token=access_token)
    except ValueError as e:
        raise click.ClickException(e)

if __name__ == '__main__':
    cli()
