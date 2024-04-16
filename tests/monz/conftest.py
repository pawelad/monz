"""monz pytest configuration and utils."""

from unittest.mock import MagicMock

import pytest
from click.testing import CliRunner
from pytest_mock import MockerFixture

from .factories import (
    MonzoAccountFactory,
    MonzoBalanceFactory,
    MonzoPotFactory,
    MonzoTransactionFactory,
    MonzoWhoAmIFactory,
)


@pytest.fixture(scope="module")
def cli_runner() -> CliRunner:
    """Return a `CliRunner` instance."""
    return CliRunner()


# TODO: Is there a better way?
@pytest.fixture()
def mocked_monzo_api(mocker: MockerFixture) -> MagicMock:
    """Return a mocked `pymonzo.MonzoAPI` instance."""
    account1 = MonzoAccountFactory.build()
    account2 = MonzoAccountFactory.build()
    balance = MonzoBalanceFactory.build()
    pot1 = MonzoPotFactory.build(deleted=False)
    pot2 = MonzoPotFactory.build(deleted=False)
    transaction1 = MonzoTransactionFactory.build()
    transaction2 = MonzoTransactionFactory.build()
    transaction3 = MonzoTransactionFactory.build()
    transaction4 = MonzoTransactionFactory.build()
    whoami = MonzoWhoAmIFactory.build()

    monzo_api = mocker.MagicMock()
    monzo_api.accounts.list.return_value = [account1, account2]
    monzo_api.balance.get.return_value = balance
    monzo_api.pots.list.return_value = [pot1, pot2]
    monzo_api.transactions.list.return_value = [
        transaction1,
        transaction2,
        transaction3,
        transaction4,
    ]
    monzo_api.whoami.return_value = whoami

    return monzo_api
