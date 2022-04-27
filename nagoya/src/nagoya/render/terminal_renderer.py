import os

from sty import bg, fg, rs

from .renderer import Buffer


def render_to_terminal(buffer: Buffer) -> None:
    scene = ""
    for y in range(len(buffer.rendered_tiles)):
        for x in range(len(buffer.rendered_tiles[y])):
            tile = buffer.rendered_tiles[y][x]
            printed_symbol = tile.object_texture.object_id
            printed_symbol = coloring_text_24bit(printed_symbol, tile.object_color.get_rgb())
            printed_symbol = coloring_background_24bit(printed_symbol, tile.background_color.get_rgb())
            scene += printed_symbol
        scene += "\n\r"
    print("\033[H\033[J")
    print(scene)


def coloring_text_24bit(text: str, color: (int, int, int)) -> str:
    r, g, b = color
    return f"{fg(r, g, b)}{text}{rs.fg}"


def coloring_background_24bit(text: str, color: (int, int, int)) -> str:
    r, g, b = color
    return f"{bg(r, g, b)}{text}{rs.bg}"
