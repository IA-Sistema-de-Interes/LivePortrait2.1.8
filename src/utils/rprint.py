# coding: utf-8
#Edit by IA (Sistema  de interes)

"""
Custom print and log functions with basic ANSI escape code styling.
"""

__all__ = ['rprint', 'rlog']

ANSI_CODES = {
    "reset": "0",
    "bold": "1",
    "underline": "4",
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37"
}

def apply_style(text, style=None):
    """Applies ANSI style codes to the given text."""
    if not style:
        return text

    style_codes = []
    for s in style.lower().split():
        if s in ANSI_CODES:
            style_codes.append(ANSI_CODES[s])

    if style_codes:
        return f"\033[{';'.join(style_codes)}m{text}\033[0m"
    else:
        return text

def rprint(*objects, style=None, sep=' ', end='\n'):
    """
    Custom print function with basic ANSI escape code styling.

    Args:
        *objects: Objects to print.
        style (str, optional): Space-separated ANSI style keywords.
                               E.g., "bold green", "underline red".
        sep (str, optional): Separator for printed objects. Defaults to ' '.
        end (str, optional): String appended after the last object. Defaults to '\n'.
    """
    print(*[apply_style(str(obj), style) for obj in objects], sep=sep, end=end)

def rlog(*objects, style=None, sep=' ', end='\n'):
    """
    Custom log function with basic ANSI escape code styling.

    Args:
        *objects: Objects to log.
        style (str, optional): ANSI style keywords (same as rprint).
        sep (str, optional): Separator for logged objects. Defaults to ' '.
        end (str, optional): String appended after the last object. Defaults to '\n'.
    """
    rprint(*objects, style=style, sep=sep, end=end)
