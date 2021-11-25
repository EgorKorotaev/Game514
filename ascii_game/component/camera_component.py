from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.vector import Vector3


@dataclass
class CameraComponent(Component):
    viewport: Vector3 = Vector3(8, 8, 4)
