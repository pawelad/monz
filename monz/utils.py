# -*- coding: utf-8 -*-
"""
monz related utils
"""
from __future__ import unicode_literals

from decimal import Decimal


def monzo_amount_to_dec(amount):
    """
    Monzo API returns monetary amount as an integer without the delimiter
    before the subunit, so '10' is in fact '0.10' and '12345' is '123.45'.

    :param amount: monetary amount
    :type amount: int
    :return converted monetary amount
    :rtype Decimal
    """
    return Decimal(amount) / Decimal(100)
