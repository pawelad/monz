"""Command line entrypoint for monz."""

import sys
from typing import Optional

from monz.command_line import cli


def main(args: Optional[list[str]] = None) -> None:
    """Run `monz`.

    Arguments:
        args: CLI arguments.
    """
    cli.main(args, "monz")


if __name__ == "__main__":
    main(sys.argv[1:])
