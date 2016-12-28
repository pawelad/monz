# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4

import pytest
from click.testing import CliRunner

from monz.command_line import cli


# Module fixtures
@pytest.fixture(scope='module')
def runner():
    """Get CliRunner"""
    return CliRunner()


# Tests
def test_incorrect_access_token(runner):
    """Test invoking the script with incorrect access token"""
    result = runner.invoke(
        cli, args=['--access-token', str(uuid4()), 'balance']
    )

    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 1


def test_accounts(runner):
    """Test invoking the script 'accounts' subcommand"""
    result = runner.invoke(
        cli, args=['accounts'],
    )

    assert result.exit_code == 0
    assert result.output
    assert result.output.startswith('Account #')
    assert result.output.count('\n') >= 3


def test_balance(runner):
    """
    Test invoking the script 'balance' subcommand, which should also be the
    default subcomand
    """
    result = runner.invoke(
        cli, args=['balance'],
    )

    assert result.exit_code == 0
    assert result.output
    assert result.output.startswith('Balance:')

    result_no_args = runner.invoke(cli)

    assert result.exit_code == result_no_args.exit_code
    assert result.output == result_no_args.output
    assert result.output.count('\n') == 2


def test_transactions(runner):
    """Test invoking the script 'transactions' subcommand"""
    for n in [1, 5, 10]:
        result = runner.invoke(
            cli, args=['transactions', '-n', str(n)],
        )

        assert result.exit_code == 0
        assert result.output
        # Each item takes 3 lines plus a blank one, no new line at the end
        assert result.output.count('\n') == (n*4 - 1)
