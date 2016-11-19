# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal


def monzo_amount_to_dec(amount):
    """
    Monzo API returns monetary amount as an integer without the delimiter
    before the subunit, so 12345 is in fact 123.45

    :param amount: monetary amount
    :type amount: int
    :return converted monetary amount
    :rtype Decimal
    """
    return Decimal(
        str(amount)[:-2] + '.' + str(amount)[-2:]
    )
