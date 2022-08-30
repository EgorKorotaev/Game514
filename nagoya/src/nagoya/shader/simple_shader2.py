from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.primitive import ColorA
from nagoya.primitive.vector import Vector3
from nagoya.render.texture import ObjectTexture

from .shader import Shader
from .shader_visitor import ShaderVisitor


class SimpleShader2(Shader):
    def __init__(self, background_color: ColorA, object_color: ColorA, object_texture: ObjectTexture):
        self.background_color = background_color
        self.object_color = object_color
        self.object_texture = object_texture
        self.sub_texture_1 = ObjectTexture("◤")
        self.sub_texture_2 = ObjectTexture("◢")

    def render(
        self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None
    ) -> RenderedTile:
        this_tile = RenderedTile(self.background_color, self.object_color, self.object_texture)

        # if underlying_tile is None:
        #     return this_tile

        self.adjust_color_to_height(this_tile, position_relative_to_camera.z)
        tile_mixed = self.mix_tiles(underlying_tile, this_tile, position_relative_to_camera)

        return tile_mixed

    def mix_tiles(
        self, underlying_tile: RenderedTile | None, tile: RenderedTile | None, config: Vector3
    ) -> RenderedTile | None:
        background_color_x = tile.background_color
        background_color_y = tile.background_color.lighten(0.4)
        background_color_z = tile.background_color.darken(0.4)

        if config.x == 0 and config.y == 0:  # 1
            background_color = background_color_x
            object_color = ColorA(a=0)
            object_texture = self.sub_texture_1

        elif config.x == 0 and config.y == 1:  # 2
            background_color = background_color_y
            object_color = ColorA(a=0)
            object_texture = ObjectTexture()

        elif config.x == 1 and config.y == 1:  # 3 центр нижний
            background_color = background_color_y
            object_color = ColorA(a=0)
            object_texture = ObjectTexture()

        elif config.x == 2 and config.y == 1:  # 4 правый нижний
            background_color = ColorA(a=0)
            object_color = background_color_z
            object_texture = self.sub_texture_1

        elif config.x == 2 and config.y == 0:  # 5
            background_color = background_color_x
            object_color = background_color_z
            object_texture = self.sub_texture_2

        elif config.x == 1 and config.y == 0:  # 6
            background_color = background_color_x
            object_color = ColorA(a=0)
            object_texture = ObjectTexture()

        else:
            background_color = ColorA(a=0)
            object_color = ColorA(a=0)
            object_texture = ObjectTexture()

        if underlying_tile is not None:
            if config.x == 0 and config.y == 0:  # 1
                if underlying_tile.object_texture != self.sub_texture_1:
                    background_color = underlying_tile.background_color + background_color
                    object_color = underlying_tile.background_color
                else:
                    # background_color = underlying_tile.object_color + background_color
                    object_color = underlying_tile.object_color
                    object_texture = underlying_tile.object_texture
                    background_color = underlying_tile.background_color + background_color

            elif config.x == 0 and config.y == 1:  # 2
                object_color = underlying_tile.object_color + background_color
                background_color = underlying_tile.background_color + background_color
                object_texture = underlying_tile.object_texture

            elif config.x == 1 and config.y == 1:  # 3
                background_color = underlying_tile.background_color + background_color
                if underlying_tile.object_texture != ObjectTexture():
                    object_color = background_color
                    object_texture = underlying_tile.object_texture

            elif config.x == 2 and config.y == 1:  # 4
                object_color = underlying_tile.object_color + object_color
                if underlying_tile.object_texture != self.sub_texture_1:
                    background_color = underlying_tile.object_color + background_color
                else:
                    background_color = underlying_tile.background_color + background_color

            elif config.x == 2 and config.y == 0:  # 5
                # object_color = underlying_tile.object_color + object_color
                if underlying_tile.object_texture == self.sub_texture_2:
                    background_color = underlying_tile.background_color + background_color
                    object_texture = underlying_tile.object_texture
                    object_color = underlying_tile.object_color + object_color
                else:
                    object_color = underlying_tile.background_color + object_color
                    background_color = underlying_tile.background_color + background_color

            elif config.x == 1 and config.y == 0:  # 6
                background_color = underlying_tile.background_color + background_color
                if underlying_tile.object_texture != self.sub_texture_1:
                    object_color = underlying_tile.object_color + object_color
                    object_texture = underlying_tile.object_texture

                if object_texture == self.sub_texture_2:
                    object_color = background_color

            # if underlying_tile.object_texture == self.sub_texture_1 or underlying_tile.object_texture == self.sub_texture_2:
            #     pass

        rendered_tile = RenderedTile(
            background_color=background_color, object_color=object_color, object_texture=object_texture
        )

        return rendered_tile

    def adjust_color_to_height(self, tile: RenderedTile, delta_z: int):
        viewport = 8
        percent = abs(delta_z / viewport)
        match delta_z:
            case _ if delta_z == 0:
                return
            case _ if delta_z < 0:
                tile.background_color = tile.background_color.darken(percent)
                tile.object_color = tile.object_color.darken(percent)
            case _ if delta_z > 0:
                tile.background_color = tile.background_color.lighten(percent)
                tile.object_color = tile.object_color.lighten(percent)

    def accept(self, visitor: ShaderVisitor):
        return visitor.visit_simple(self)

    @staticmethod
    def create_simple_shader_2(
        background_color: ColorA = ColorA(),
        object_color: ColorA = ColorA(),
        object_texture: ObjectTexture = ObjectTexture(),
    ) -> "SimpleShader2":
        return SimpleShader2(background_color, object_color, object_texture)
