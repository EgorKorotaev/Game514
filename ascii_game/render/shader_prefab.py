from enum import Enum
from typing import NamedTuple

from ascii_game.render.colored_text import ANSIColor
from ascii_game.render.shader import CustomShader, Shader
from ascii_game.render.texture import BackgroundColor, ObjectColor, ObjectTexture

player = CustomShader(
    background_color=BackgroundColor(""), object_color=ObjectColor(ANSIColor.CYAN), object_texture=ObjectTexture("👻")
)

wheat = CustomShader(
    background_color=BackgroundColor(""), object_color=ObjectColor(ANSIColor.YELLOW), object_texture=ObjectTexture("🌾")
)

field = CustomShader(
    background_color=BackgroundColor(ANSIColor.BLACK), object_color=ObjectColor(""), object_texture=ObjectTexture("")
)


class _Shaders(NamedTuple):
    shader: Shader


class ShadersPrefab(_Shaders, Enum):
    PLAYER = _Shaders(player)
    WHEAT = _Shaders(wheat)
    FIELD = _Shaders(field)


def get_shader(shaders_prefab: ShadersPrefab) -> Shader:
    return shaders_prefab.shader
