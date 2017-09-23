#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line entry point for monz
"""
from __future__ import unicode_literals

import sys

from monz.command_line import cli


def main(args=None):
    """Run monz"""
    cli.main(args, 'monz')


if __name__ == '__main__':
    main(sys.argv[1:])
