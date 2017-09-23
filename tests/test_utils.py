# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from decimal import Decimal

from monz.utils import monzo_amount_to_dec


@pytest.mark.parametrize('arg,result', [
    (123, Decimal('1.23')),
    (1234, Decimal('12.34')),
    (12345, Decimal('123.45')),
])
def test_monzo_str_to_dec(arg, result):
    """Test monz.utils.monzo_amount_to_dec"""
    assert monzo_amount_to_dec(arg) == result
