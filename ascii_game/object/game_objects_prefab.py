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
    game_object = GameObject.create_game_object()
    game_object.add_component(
        RendererComponent.create_renderer_component(game_object, shader=get_shader(ShadersPrefab.PLAYER))
    )
    game_object.get_component(RendererComponent).priority = 1000
    return game_object


def _glass_prefab() -> GameObject:
    game_object = GameObject.create_game_object()
    glass_shader = TransparentShader(ColorA(0, 1, 0, a=0.2))
    game_object.add_component(RendererComponent.create_renderer_component(game_object, shader=glass_shader))
    game_object.get_component(RendererComponent).priority = 11
    return game_object


def _wheat_prefab() -> GameObject:
    game_object = GameObject.create_game_object()
    game_object.add_component(
        RendererComponent.create_renderer_component(game_object, shader=get_shader(ShadersPrefab.WHEAT))
    )
    game_object.get_component(RendererComponent).priority = 50
    return game_object


def _field_prefab() -> GameObject:
    game_object = GameObject.create_game_object()
    game_object.add_component(
        RendererComponent.create_renderer_component(game_object, shader=get_shader(ShadersPrefab.FIELD))
    )
    game_object.get_component(RendererComponent).priority = 10
    return game_object


def _dark_smoke_prefab() -> GameObject:
    game_object = GameObject.create_game_object()
    game_object.add_component(
        RendererComponent.create_renderer_component(game_object, shader=get_shader(ShadersPrefab.DARK_SMOKE))
    )
    return game_object


def _light_smoke_prefab() -> GameObject:
    game_object = GameObject.create_game_object()
    game_object.add_component(
        RendererComponent.create_renderer_component(game_object, shader=get_shader(ShadersPrefab.LIGHT_SMOKE))
    )
    return game_object


def _air_prefab() -> GameObject:
    game_object = GameObject.create_game_object()
    game_object.add_component(
        RendererComponent.create_renderer_component(game_object, shader=get_shader(ShadersPrefab.AIR))
    )
    return game_object
