from sty import bg, rs, fg


def coloring_text_24bit(text: str, color: (int, int, int)) -> str:
    r, g, b = color
    return f"{fg(r, g, b)}{text}{rs.fg}"


def coloring_background_24bit(text: str, color: (int, int, int)) -> str:
    r, g, b = color
    return f"{bg(r, g, b)}{text}{rs.bg}"
