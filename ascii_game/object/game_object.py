from typing import NewType, Type, cast

from ascii_game.component.component import Component
from ascii_game.component.transform_component import TransformComponent

GameObjectId = NewType("GameObjectId", int)


class GameObject:
    def __init__(self):
        self._components: dict[Type[Component], Component] = {}

    @property
    def transform(self) -> TransformComponent:
        return cast(TransformComponent, self._components[TransformComponent])

    def add_component(self, component: Component):
        self._components[type(component)] = component
        component.init()

    def get_component(self, component_type: Type[Component]) -> Component | None:
        return self._components.get(component_type)

    def init(self) -> None:
        for component in self._components.values():
            component.init()

    @staticmethod
    def create_game_object() -> "GameObject":
        game_object = GameObject()
        game_object.add_component(TransformComponent(game_object))
        return game_object
