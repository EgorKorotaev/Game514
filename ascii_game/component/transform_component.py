from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.vector import Vector3


@dataclass
class TransformComponent(Component):
    position: Vector3 = Vector3()
