"""monz test utils."""

import io

from rich.console import Console, RenderableType


def renderable_to_str(obj: RenderableType) -> str:
    """Render passed `RenderableType` to a string."""
    console = Console(file=io.StringIO(), width=120)
    console.print(obj)
    output = console.file.getvalue()
    return output
