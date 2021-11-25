from enum import Enum, auto
from typing import NamedTuple

from ascii_game.component.renderer_component import RendererComponent
from ascii_game.component.renderer_priority import RendererPriority
from ascii_game.object.game_object import GameObject
from ascii_game.render.shader_prefab import ShadersPrefab, get_shader

class _GameObjects(NamedTuple):
    game_object: GameObject


class GameObjectsPrefab(Enum):
    PLAYER = auto()
    WHEAT = auto()
    FIELD = auto()


def get_game_object(game_objects_prefab: GameObjectsPrefab) -> GameObject:  # TODO возвращает новый объект
    match game_objects_prefab:
        case GameObjectsPrefab.PLAYER:
            return player_prefab()
        case GameObjectsPrefab.WHEAT:
            return wheat_prefab()
        case GameObjectsPrefab.FIELD:
            return field_prefab()



def player_prefab() -> GameObject:
    player = GameObject()
    player.add_component(RendererComponent(get_shader(ShadersPrefab.PLAYER)))
    player.add_component(RendererPriority(1000))
    return player


def wheat_prefab() -> GameObject:
    wheat = GameObject()
    wheat.add_component(RendererComponent(get_shader(ShadersPrefab.WHEAT)))
    wheat.add_component(RendererPriority(50))
    return wheat


def field_prefab() -> GameObject:
    field = GameObject()
    field.add_component(RendererComponent(get_shader(ShadersPrefab.FIELD)))
    field.add_component(RendererPriority(10))  # TODO в рендерер
    return field