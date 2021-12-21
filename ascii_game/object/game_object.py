from dataclasses import dataclass, field
from typing import NewType, Type

from ascii_game.component.component import Component
from ascii_game.component.transform_component import TransformComponent
from ascii_game.save.saving_visitor import JSONExportComponentVisitor

GameObjectId = NewType("GameObjectId", int)


@dataclass
class GameObject:
    _components: dict[Type[Component], Component] = field(default_factory=dict)
    transform: TransformComponent = field(default_factory=TransformComponent)

    def add_component(self, component: Component):
        self._components[type(component)] = component

    def get_component(self, component_type: Type[Component]) -> Component | None:
        return self._components.get(component_type)

    def saving(self) -> dict:
        json_export_component_visitor = JSONExportComponentVisitor()
        data = {
            'transform': self.transform.accept(json_export_component_visitor),
            '_components': [self._components[key].accept(json_export_component_visitor) for key in self._components.keys()]
        }
        return data
