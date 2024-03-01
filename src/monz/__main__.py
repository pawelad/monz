"""Command line entrypoint for monz."""

import sys
from typing import List, Optional

from monz.command_line import cli


def main(args: Optional[List[str]] = None) -> None:
    """Run `monz`.

    Arguments:
        args: CLI arguments.
    """
    cli.main(args, "monz")


if __name__ == "__main__":
    main(sys.argv[1:])
