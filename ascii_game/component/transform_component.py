from dataclasses import dataclass, field

from ascii_game.component.component import Component
from ascii_game.visitor import ComponentVisitor
from ascii_game.primitive.vector import Vector3


@dataclass
class TransformComponent(Component):
    position: Vector3 = field(default_factory=Vector3)

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_transform(self)
