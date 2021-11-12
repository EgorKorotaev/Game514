from dataclasses import dataclass

from ascii_game.component import PhysicalComponent, GraphicComponent
from ascii_game.vector import Vector3


@dataclass
class PositionComponent:
    position: Vector3 = Vector3()


@dataclass
class GameObject:
    physicalObject: PhysicalComponent = PhysicalComponent()
    graphicObject: GraphicComponent = GraphicComponent()
    transform: PositionComponent = PositionComponent()
    id: str = ""
