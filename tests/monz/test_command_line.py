"""Test `monz.command_line` module."""

from datetime import datetime, timedelta
from unittest.mock import MagicMock

from click.testing import CliRunner
from pytest_mock import MockerFixture
from time_machine import TimeMachineFixture

from monz.command_line import cli

from .utils import renderable_to_str


def test_info(
    mocker: MockerFixture,
    time_machine: TimeMachineFixture,
    cli_runner: CliRunner,
    mocked_monzo_api: MagicMock,
) -> None:
    """Outputs account balance and latest transaction."""
    time_machine.move_to(datetime(2024, 3, 1), tick=False)

    mocked_MonzoAPI = mocker.patch(  # noqa
        "monz.command_line.MonzoAPI",
        autospec=True,
        return_value=mocked_monzo_api,
    )

    result = cli_runner.invoke(cli, args=["info"])

    mocked_MonzoAPI.assert_called_once_with(access_token=None)
    mocked_monzo_api.balance.get.assert_called_once_with(account_id=None)
    mocked_monzo_api.transactions.list.assert_called_once_with(
        account_id=None,
        expand_merchant=True,
        since=datetime.now() - timedelta(days=30),
    )

    assert result.exit_code == 0
    assert result.output

    balance = mocked_monzo_api.balance.get()
    assert renderable_to_str(balance) in result.output

    transactions = mocked_monzo_api.transactions.list()
    assert renderable_to_str(transactions[-1]) in result.output
    for transaction in transactions[:-1]:
        assert renderable_to_str(transaction) not in result.output

    # Running the script with no arguments should have the same effect
    result_no_args = cli_runner.invoke(cli)

    assert result.exit_code == result_no_args.exit_code
    assert result.output == result_no_args.output


def test_whoami(
    mocker: MockerFixture,
    cli_runner: CliRunner,
    mocked_monzo_api: MagicMock,
) -> None:
    """Outputs `whoami` data."""
    mocked_MonzoAPI = mocker.patch(  # noqa
        "monz.command_line.MonzoAPI",
        autospec=True,
        return_value=mocked_monzo_api,
    )

    result = cli_runner.invoke(cli, args=["whoami"])

    mocked_MonzoAPI.assert_called_once_with(access_token=None)
    mocked_monzo_api.whoami.assert_called_once_with()

    assert result.exit_code == 0
    assert result.output

    whoami = mocked_monzo_api.whoami()
    assert renderable_to_str(whoami) in result.output


def test_accounts(
    mocker: MockerFixture,
    cli_runner: CliRunner,
    mocked_monzo_api: MagicMock,
) -> None:
    """Outputs user accounts."""
    mocked_MonzoAPI = mocker.patch(  # noqa
        "monz.command_line.MonzoAPI",
        autospec=True,
        return_value=mocked_monzo_api,
    )

    result = cli_runner.invoke(cli, args=["accounts"])

    mocked_MonzoAPI.assert_called_once_with(access_token=None)
    mocked_monzo_api.accounts.list.assert_called_once_with()

    assert result.exit_code == 0
    assert result.output

    accounts = mocked_monzo_api.accounts.list()
    for account in accounts:
        assert renderable_to_str(account) in result.output


def test_balance(
    mocker: MockerFixture,
    cli_runner: CliRunner,
    mocked_monzo_api: MagicMock,
) -> None:
    """Outputs user balance."""
    mocked_MonzoAPI = mocker.patch(  # noqa
        "monz.command_line.MonzoAPI",
        autospec=True,
        return_value=mocked_monzo_api,
    )

    result = cli_runner.invoke(cli, args=["balance"])

    mocked_MonzoAPI.assert_called_once_with(access_token=None)
    mocked_monzo_api.balance.get.assert_called_once_with(account_id=None)

    assert result.exit_code == 0
    assert result.output

    balance = mocked_monzo_api.balance.get()
    assert renderable_to_str(balance) in result.output

    # TODO: Test `--account_id` option


def test_transactions(
    mocker: MockerFixture,
    time_machine: TimeMachineFixture,
    cli_runner: CliRunner,
    mocked_monzo_api: MagicMock,
) -> None:
    """Outputs user transactions."""
    time_machine.move_to(datetime(2024, 3, 1), tick=False)

    mocked_MonzoAPI = mocker.patch(  # noqa
        "monz.command_line.MonzoAPI",
        autospec=True,
        return_value=mocked_monzo_api,
    )

    result = cli_runner.invoke(cli, args=["transactions"])

    mocked_MonzoAPI.assert_called_once_with(access_token=None)
    mocked_monzo_api.transactions.list.assert_called_once_with(
        account_id=None,
        expand_merchant=True,
        since=datetime.now() - timedelta(days=30),
    )

    assert result.exit_code == 0
    assert result.output

    transactions = mocked_monzo_api.transactions.list()
    for transaction in transactions[-3:]:
        assert renderable_to_str(transaction) in result.output

    for transaction in transactions[:-3]:
        assert renderable_to_str(transaction) not in result.output

    # TODO: Test `--account_id` option
    # TODO: Test `--num` option
