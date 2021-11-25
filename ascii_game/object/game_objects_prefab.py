from enum import Enum
from typing import NamedTuple

from ascii_game.component.renderer_component import RendererComponent
from ascii_game.component.renderer_priority import RendererPriority
from ascii_game.object.game_object import GameObject
from ascii_game.render.shader_prefab import ShadersPrefab, get_shader

player = GameObject()
player.add_component(RendererComponent(get_shader(ShadersPrefab.PLAYER)))
player.add_component(RendererPriority(1000))

wheat = GameObject()
wheat.add_component(RendererComponent(get_shader(ShadersPrefab.WHEAT)))
wheat.add_component(RendererPriority(50))

field = GameObject()
field.add_component(RendererComponent(get_shader(ShadersPrefab.FIELD)))
field.add_component(RendererPriority(10))  # TODO в рендерер


class _GameObjects(NamedTuple):
    game_object: GameObject


class GameObjectsPrefab(_GameObjects, Enum):
    PLAYER = _GameObjects(player)
    WHEAT = _GameObjects(wheat)
    FIELD = _GameObjects(field)


def get_game_object(GameObjectsPrefab: GameObjectsPrefab) -> GameObject:
    return getattr(GameObjectsPrefab, "game_object")
