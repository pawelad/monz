"""monz factories."""

from polyfactory.factories.pydantic_factory import ModelFactory
from pymonzo.accounts import MonzoAccount
from pymonzo.balance import MonzoBalance
from pymonzo.transactions import MonzoTransaction
from pymonzo.whoami import MonzoWhoAmI


class MonzoAccountFactory(ModelFactory[MonzoAccount]):
    """Factory for `MonzoAccount` schema."""


class MonzoBalanceFactory(ModelFactory[MonzoBalance]):
    """Factory for `MonzoBalance` schema."""


class MonzoTransactionFactory(ModelFactory[MonzoTransaction]):
    """Factory for `MonzoTransaction` schema."""


class MonzoWhoAmIFactory(ModelFactory[MonzoWhoAmI]):
    """Factory for `MonzoWhoAmI` schema."""
