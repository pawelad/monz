# -*- coding: utf-8 -*-
"""
Test 'monz.utils' file
"""
from __future__ import unicode_literals

import pytest
from decimal import Decimal

from monz.utils import monzo_amount_to_dec


@pytest.mark.parametrize('arg,result', [
    (-12345, '-123.45'),
    (-1234, '-12.34'),
    (-123, '-1.23'),
    (-12, '-0.12'),
    (-1, '-0.01'),
    (0, '0.00'),
    (1, '0.01'),
    (12, '0.12'),
    (123, '1.23'),
    (1234, '12.34'),
    (12345, '123.45'),
])
def test_monzo_str_to_dec_function(arg, result):
    """Test monz.utils.monzo_amount_to_dec function"""
    assert monzo_amount_to_dec(arg) == Decimal(result)
