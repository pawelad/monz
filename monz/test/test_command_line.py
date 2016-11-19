# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from uuid import uuid4

import pytest
from click.testing import CliRunner

from monz.command_line import cli
from pymonzo.monzo_api import MONZO_ACCESS_TOKEN


# Module fixtures
@pytest.fixture(scope='module')
def runner():
    """Get CliRunner"""
    return CliRunner()


# Tests
def test_no_access_token(monkeypatch, runner):
    """Test invoking the script without the access token"""
    monkeypatch.delenv(MONZO_ACCESS_TOKEN, raising=False)

    result = runner.invoke(cli)

    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 1


def test_incorrect_access_token(monkeypatch, runner):
    """Test invoking the script with incorrect access token"""
    monkeypatch.setenv(MONZO_ACCESS_TOKEN, str(uuid4()))

    result = runner.invoke(cli)

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


def test_transactions(runner):
    """Test invoking the script 'transactions' subcommand"""
    for n in [1, 5]:
        result = runner.invoke(
            cli, args=['transactions', '-n', str(n)],
        )

        assert result.exit_code == 0
        assert result.output
        assert result.output.count('\n') == (n*4 - 1)
