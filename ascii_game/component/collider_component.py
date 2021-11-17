from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.vector import Vector3


@dataclass
class ColliderComponent(Component):
    map_range: Vector3 = Vector3(1, 1, 1)
