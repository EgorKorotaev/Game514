from bearlibterminal import terminal

from .renderer import Buffer
from .renderer2 import Buffer2


def render_to_terminal(buffer: Buffer | Buffer2) -> None:
    y_len_buffer_rendered_tiles = len(buffer.rendered_tiles)
    for y in range(y_len_buffer_rendered_tiles):
        for x in range(len(buffer.rendered_tiles[y])):
            tile = buffer.rendered_tiles[y][x]
            object_texture = tile.object_texture.object_id
            if tile.object_texture.object_id == "":
                object_texture = " "
            terminal.bkcolor(tile.background_color.get_rgba_hex())
            terminal.color(tile.object_color.get_rgba_hex())
            terminal.put(int(x + 1), int(y_len_buffer_rendered_tiles - y), object_texture)
    terminal.refresh()
