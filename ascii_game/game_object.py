from dataclasses import dataclass
from typing import NewType, Type, TypeVar

from ascii_game.component.component import Component
from ascii_game.component.transform_component import TransformComponent

GameObjectId = NewType("GameObjectId", int)


@dataclass
class GameObject:
    _game_object_id: GameObjectId
    _components: dict[Type[Component], Component]
    transform: TransformComponent

    def __init__(self, game_object_id: GameObjectId):
        self._game_object_id = game_object_id
        self.transform = TransformComponent()

    def add_component(self, component: Component):
        self._components[type(component)] = component

    def get_component(self, component_type: Type[Component]) -> Component | None:
        return self._components.get(component_type)
