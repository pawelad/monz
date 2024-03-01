"""monz utils."""

from click_default_group import DefaultGroup
from rich_click import RichGroup


class DefaultRichGroup(DefaultGroup, RichGroup):
    """Make `click-default-group` work with `rick-click`."""
