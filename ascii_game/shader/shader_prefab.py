from enum import Enum, auto
from typing import NamedTuple
import html

from ascii_game.primitive.color_a import ColorA
from ascii_game.shader.shader import Shader
from ascii_game.shader.simple_shader import SimpleShader
from ascii_game.render.texture import ObjectTexture


class _Shaders(NamedTuple):
    shader: Shader


class ShadersPrefab(_Shaders, Enum):
    PLAYER = auto()
    GLASS = auto()
    WHEAT = auto()
    FIELD = auto()
    DARK_SMOKE = auto()
    LIGHT_SMOKE = auto()
    AIR = auto()


def get_shader(shader_prefab: ShadersPrefab) -> Shader:
    match shader_prefab:
        case ShadersPrefab.PLAYER:
            return _player_prefab()
        case ShadersPrefab.GLASS:
            return _glass_prefab()
        case ShadersPrefab.WHEAT:
            return _wheat_prefab()
        case ShadersPrefab.FIELD:
            return _field_prefab()
        case ShadersPrefab.DARK_SMOKE:
            return _dark_smoke_prefab()
        case ShadersPrefab.LIGHT_SMOKE:
            return _light_smoke_prefab()
        case ShadersPrefab.AIR:
            return _air_prefab()


def _player_prefab() -> Shader:
    object_color = ColorA()
    object_color.set_rgb(0, 1, 1)
    player = SimpleShader(
        background_color=ColorA(0, 0, 0, a=0),
        object_color=object_color,
        # object_texture=ObjectTexture(html.unescape('&#129503;'))
        object_texture=ObjectTexture("🤺")
        # "🌾"
    )
    return player


def _glass_prefab() -> Shader:
    color = ColorA()
    color.set_rgb(0, 1, 0)
    # h, _, _ = background_color.get_hsl()
    # background_color.set_hsl(h, 1, 0.7)
    color.a = 0.8
    player = SimpleShader(
        background_color=color,
        object_color=color,
        # object_texture=ObjectTexture(html.unescape('&#129503;'))
        object_texture=ObjectTexture(),
    )
    return player


def _wheat_prefab() -> Shader:
    object_color = ColorA()
    object_color.set_rgb(1, 1, 0)
    wheat = SimpleShader(
        background_color=ColorA(0, 0, 0, a=0),
        object_color=object_color,
        object_texture=ObjectTexture(html.unescape("&#127806;")),  # 🌾
    )
    return wheat


def _field_prefab() -> Shader:
    background_color = ColorA()
    background_color.set_rgb_255(162, 101, 62)
    field = SimpleShader(
        background_color=background_color, object_color=ColorA(0, 0, 0, a=0), object_texture=ObjectTexture()
    )
    return field


def _dark_smoke_prefab() -> Shader:
    color = ColorA()
    color.a = 0.2
    color.set_hsl(0, 0, 0)
    dark_smoke = SimpleShader(background_color=color, object_color=color, object_texture=ObjectTexture())
    return dark_smoke


def _light_smoke_prefab() -> Shader:
    color = ColorA()
    color.a = 0.2
    color.set_hsl(0, 0, 1)
    light_smoke = SimpleShader(background_color=color, object_color=color, object_texture=ObjectTexture())
    return light_smoke


def _air_prefab() -> Shader:
    color = ColorA()
    color.a = 1
    color.set_rgb(0.5, 0.5, 0.5)
    air = SimpleShader(background_color=color, object_color=color, object_texture=ObjectTexture("  "))
    return air
