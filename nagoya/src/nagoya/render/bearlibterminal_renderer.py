from bearlibterminal import terminal

from .renderer import Buffer


def render_to_terminal(buffer: Buffer) -> None:
    for y in range(len(buffer.rendered_tiles)):
        for x in range(len(buffer.rendered_tiles[y])):
            tile = buffer.rendered_tiles[y][x]
            object_texture = tile.object_texture.object_id
            if tile.object_texture.object_id == "":
                object_texture = " "
            terminal.bkcolor(tile.background_color.get_rgba_hex())
            terminal.color(tile.object_color.get_rgba_hex())
            terminal.put(x, buffer.viewport.y - 1 - y, object_texture)
    terminal.refresh()
