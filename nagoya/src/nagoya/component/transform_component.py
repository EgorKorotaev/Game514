from nagoya.primitive.vector import Vector3

from .component import Component
from .component_visitor import ComponentVisitor


class TransformComponent(Component):
    def __init__(self, game_object: "GameObject", position: Vector3 = None):
        super().__init__(game_object)
        self.position = position or Vector3()

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_transform(self)

    def init(self) -> None:
        pass
