from typing import Any

from ascii_game.component.component import Component
from ascii_game.component.keyboard_subject_component import KeyboardEvent
from ascii_game.event_system.event_manager import Event
from ascii_game.object.game_object import GameObject
from ascii_game.primitive.vector import Vector2, Vector3
from ascii_game.visitor import ComponentVisitor


class PlayerController(Component):
    def accept(self, visitor: ComponentVisitor) -> Any:
        pass

    def init(self):
        game_object: GameObject = self.this_game_object()

        def event_listener(event: Event):
            direction = _get_direction(event.payload())
            game_object.transform.position += Vector3(direction.x, direction.y, 0)

        event_manager = self.get_event_manager()
        event_manager.attach(KeyboardEvent.name(), event_listener)


def _get_direction(key: str) -> Vector2:
    match key:
        case "1":
            direction = Vector2(-1, -1)
        case "2":
            direction = Vector2(0, -1)
        case "3":
            direction = Vector2(1, -1)
        case "6":
            direction = Vector2(1, 0)
        case "9":
            direction = Vector2(1, 1)
        case "8":
            direction = Vector2(0, 1)
        case "7":
            direction = Vector2(-1, 1)
        case "4":
            direction = Vector2(-1, 0)
        case _:
            direction = Vector2(0, 0)
    return direction
