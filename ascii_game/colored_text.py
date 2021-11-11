from enum import Enum
from typing import NamedTuple


class _ColorCodes(NamedTuple):
    text_color_code: str
    background_color_code: str


class ANSIColor(_ColorCodes, Enum):
    BLACK = _ColorCodes("\033[30m", "\033[40m")
    RED = _ColorCodes("\033[31m", "\033[41m")
    GREEN = _ColorCodes("\033[32m", "\033[42m")
    YELLOW = _ColorCodes("\033[33m", "\033[43m")
    BLUE = _ColorCodes("\033[34m", "\033[44m")
    MAGENTA = _ColorCodes("\033[35m", "\033[45m")
    CYAN = _ColorCodes("\033[36m", "\033[46m")
    WHITE = _ColorCodes("\033[37m", "\033[47m")


def colored_text(text: str, color: ANSIColor):
    return f"{color.text_color_code}{text}"


def colored_background(text: str, color: ANSIColor):
    return f"{color.background_color_code}{text}"
