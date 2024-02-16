#!/usr/bin/env python
"""
Command line entry point for monz
"""

import sys

from monz.command_line import cli


def main(args=None):
    """Run monz"""
    cli.main(args, 'monz')


if __name__ == '__main__':
    main(sys.argv[1:])
