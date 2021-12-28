from abc import ABC, abstractmethod
from typing import Any, Type

from .component_visitor import ComponentVisitor
from .component import Component
from nagoya.object.game_object import GameObject


def custom_component(component_class):
    register_component(component_class)
    return component_class

#
# class CustomComponentMeta(Component.__metaclass__, ABC.__metaclass__):
#     def __init__(cls, name, bases, clsdict):
#         print(name)
#         super(CustomComponentMeta, cls).__init__(name, bases, clsdict)
#

class CustomComponent(Component, ABC):
    def accept(self, visitor: ComponentVisitor) -> Any:
        visitor.visit_custom_component(self)

    @abstractmethod
    def params_to_json(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def load_from_json(game_object: GameObject, params: dict) -> 'CustomComponent':
        pass


_components: dict[str, Type[CustomComponent]] = {}


def register_component(custom_component: Type[CustomComponent]) -> None:
    _components[custom_component.__name__] = custom_component


def get_component(component_name: str) -> Type[CustomComponent]:
    return _components[component_name]  # TODO пуксть падоет с правильной ошибкой если не находит
