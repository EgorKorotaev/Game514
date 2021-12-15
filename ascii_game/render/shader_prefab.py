from enum import Enum, auto
from typing import NamedTuple

from ascii_game.render.ansi_colored_text import ANSIColor
from ascii_game.render.color_a import ColorA
from ascii_game.render.shader import DefaultShader, Shader
from ascii_game.render.texture import BackgroundColor, ObjectColor, ObjectTexture

class _Shaders(NamedTuple):
    shader: Shader


class ShadersPrefab(_Shaders, Enum):
    PLAYER = auto()
    WHEAT = auto()
    FIELD = auto()


def get_shader(shader_prefab: ShadersPrefab) -> Shader:
    match shader_prefab:
        case ShadersPrefab.PLAYER:
            return player_prefab()
        case ShadersPrefab.WHEAT:
            return wheat_prefab()
        case ShadersPrefab.FIELD:
            return field_prefab()



def player_prefab() -> Shader:
    background_color = ColorA()
    background_color.set_rgb(0, 1, 1)
    background_color.set_hsl(background_color.h, 1, 0.7)
    background_color.a = 0.1
    object_color = ColorA()
    object_color.set_rgb(0, 1, 1)
    player = DefaultShader(
        background_color=BackgroundColor(background_color),
        object_color=ObjectColor(object_color),
        object_texture=ObjectTexture("👻")
    )
    return player


def wheat_prefab() -> Shader:
    object_color = ColorA()
    object_color.set_rgb(1, 1, 0)
    wheat = DefaultShader(
        background_color=BackgroundColor(),
        object_color=ObjectColor(object_color),
        object_texture=ObjectTexture("🌾")
    )
    return wheat


def field_prefab() -> Shader:
    background_color = ColorA()
    background_color.set_rgb_255(162, 101, 62)
    field = DefaultShader(
        background_color=BackgroundColor(background_color),
        object_color=ObjectColor(),
        object_texture=ObjectTexture("")
    )
    return field
