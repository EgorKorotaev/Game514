from enum import Enum, auto
from typing import NamedTuple

from ascii_game.component.renderer_component import RendererComponent
from ascii_game.object.game_object import GameObject
from ascii_game.primitive.color_a import ColorA
from ascii_game.shader.transparent_shader import TransparentShader
from ascii_game.shader.shader_prefab import ShadersPrefab, get_shader

class _GameObjects(NamedTuple):
    game_object: GameObject


class GameObjectsPrefab(Enum):
    PLAYER = auto()
    GLASS = auto()
    WHEAT = auto()
    FIELD = auto()
    DARK_SMOKE = auto()
    LIGHT_SMOKE = auto()
    AIR = auto()


def get_game_object(game_objects_prefab: GameObjectsPrefab) -> GameObject:
    match game_objects_prefab:
        case GameObjectsPrefab.PLAYER:
            return _player_prefab()
        case GameObjectsPrefab.GLASS:
            return _glass_prefab()
        case GameObjectsPrefab.WHEAT:
            return _wheat_prefab()
        case GameObjectsPrefab.FIELD:
            return _field_prefab()
        case GameObjectsPrefab.DARK_SMOKE:
            return _dark_smoke_prefab()
        case GameObjectsPrefab.LIGHT_SMOKE:
            return _light_smoke_prefab()
        case GameObjectsPrefab.AIR:
            return _air_prefab()



def _player_prefab() -> GameObject:
    player = GameObject()
    player.add_component(RendererComponent(shader=get_shader(ShadersPrefab.PLAYER), priority=1000))
    return player

def _glass_prefab() -> GameObject:
    glass = GameObject()
    glass_shader = TransparentShader(ColorA(0, 1, 0 , a=0.2))
    glass.add_component(RendererComponent(shader=glass_shader, priority=11))
    return glass


def _wheat_prefab() -> GameObject:
    wheat = GameObject()
    wheat.add_component(RendererComponent(shader=get_shader(ShadersPrefab.WHEAT), priority=50))
    return wheat


def _field_prefab() -> GameObject:
    field = GameObject()
    field.add_component(RendererComponent(shader=get_shader(ShadersPrefab.FIELD), priority=10))
    return field


def _dark_smoke_prefab() -> GameObject:
    dark_smoke = GameObject()
    dark_smoke.add_component(RendererComponent(shader=get_shader(ShadersPrefab.DARK_SMOKE)))
    return dark_smoke


def _light_smoke_prefab() -> GameObject:
    light_smoke = GameObject()
    light_smoke.add_component(RendererComponent(shader=get_shader(ShadersPrefab.LIGHT_SMOKE)))
    return light_smoke


def _air_prefab() -> GameObject:
    air = GameObject()
    air.add_component(RendererComponent(shader=get_shader(ShadersPrefab.AIR)))
    return air
