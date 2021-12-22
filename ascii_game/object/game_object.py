from dataclasses import dataclass, field
from typing import NewType, Type

from ascii_game.component.component import Component
from ascii_game.component.transform_component import TransformComponent

GameObjectId = NewType("GameObjectId", int)


class GameObject:
    def __init__(self, transform: TransformComponent, components: dict[Type[Component], Component]):
        self.transform = transform
        self._components = components

    def add_component(self, component: Component):
        self._components[type(component)] = component

    def get_component(self, component_type: Type[Component]) -> Component | None:
        return self._components.get(component_type)

    @staticmethod
    def create_game_object() -> "GameObject":
        return GameObject(transform=TransformComponent(), components={})
