from structlog import get_logger

from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.primitive import ColorA
from nagoya.primitive.vector import Vector3
from nagoya.render.texture import ObjectTexture

from .shader import Shader
from .shader_visitor import ShaderVisitor

logger = get_logger(__name__)


class CompromiseShader(Shader):
    def __init__(self, background_color: ColorA, object_color: ColorA, object_texture: ObjectTexture):
        self.background_color = background_color
        self.object_color = object_color
        self.object_texture = object_texture

    def render(
        self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None
    ) -> RenderedTile:
        tile = RenderedTile(self.background_color, self.object_color, self.object_texture)

        if underlying_tile is None:
            return tile

        # tile = self.adjust_color_and_texture_to_height(tile, position_relative_to_camera.z)
        tile = self.mix_tiles(underlying_tile, tile, position_relative_to_camera.z)
        return tile

    def mix_tiles(self, underlying_tile: RenderedTile, tile: RenderedTile, delta_z: int) -> RenderedTile:
        background_color = underlying_tile.background_color + tile.background_color
        object_color = tile.object_color
        object_texture = tile.object_texture
        rendered_tile = RenderedTile(background_color, object_color, object_texture)

        match delta_z:
            case _ if delta_z < 0:
                # object_color = background_color
                rendered_tile.object_color = rendered_tile.background_color
                rendered_tile.background_color = rendered_tile.background_color.darken(0.4)
                rendered_tile.object_texture = ObjectTexture("⌗")

            case _ if delta_z == 0:
                if rendered_tile.object_texture.object_id == "":
                    if underlying_tile.object_texture.object_id != "⌗":
                        rendered_tile.object_texture = underlying_tile.object_texture
                        rendered_tile.object_color = underlying_tile.object_color

            case _ if delta_z > 0:
                # if tile.object_texture.object_id == "":
                rendered_tile.background_color = rendered_tile.background_color
                rendered_tile.object_color = rendered_tile.background_color.darken(0.4)
                rendered_tile.object_texture = ObjectTexture("▨")

        return rendered_tile

    def adjust_color_and_texture_to_height(self, tile: RenderedTile, delta_z: int) -> RenderedTile:
        pass
        # background_color = tile.background_color
        # object_color = tile.object_color
        # object_texture = tile.object_texture
        #
        # if object_texture.object_id == '⌗':
        #     return RenderedTile(background_color, object_color, object_texture)
        #
        # match delta_z:
        #     case _ if delta_z < -1:
        #         object_color = (ColorA(a=0))
        #         background_color = (ColorA(a=0))
        #
        #     case _ if delta_z == -1:
        #         # object_color = background_color
        #         background_color = background_color.darken(0.6)
        #         # object_texture.object_id = '⌗'
        #
        #     # case _ if delta_z == 0:
        #     #     pass
        #
        #     case _ if delta_z == 1:
        #         background_color = background_color.lighten(0.9)
        #         # background_color = ColorA(a=0)
        #         object_color = background_color
        #         object_texture.object_id = '▨'
        #
        #     case _ if delta_z > 1:
        #         object_color = (ColorA(a=0))
        #         background_color = (ColorA(a=0))
        #
        # adjust_tile = RenderedTile(background_color, object_color, object_texture)
        #
        # return adjust_tile

    def accept(self, visitor: ShaderVisitor):
        return visitor.visit_compromise(self)

    @staticmethod
    def create_simple_shader(
        background_color: ColorA = ColorA(),
        object_color: ColorA = ColorA(),
        object_texture: ObjectTexture = ObjectTexture(),
    ) -> "CompromiseShader":
        return CompromiseShader(background_color, object_color, object_texture)
