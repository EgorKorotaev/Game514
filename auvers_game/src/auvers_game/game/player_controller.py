from typing import Any

from structlog import get_logger

from nagoya.component.component_visitor import ComponentVisitor
from nagoya.component.custom_component import CustomComponent, custom_component
from nagoya.component.keyboard_subject_component import KeyboardEvent
from nagoya.event_system.event_manager import Event
from nagoya.object.game_object import GameObject
from nagoya.primitive.vector import Vector2, Vector3

logger = get_logger(__name__)


@custom_component
class PlayerController(CustomComponent):
    def __init__(self, game_object: GameObject):
        super().__init__(game_object)

    def accept(self, visitor: ComponentVisitor) -> Any:
        return visitor.visit_player_controller(self)

    def init(self):
        game_object: GameObject = self.this_game_object()

        def event_listener(event: Event):
            direction = _get_direction(event.payload())
            game_object.transform.position += direction
            logger.debug(
                "new position",
                x=game_object.transform.position.x,
                y=game_object.transform.position.y,
                z=game_object.transform.position.z,
            )

        event_manager = self.get_event_manager()
        event_manager.attach(KeyboardEvent.name(), event_listener)

    def params_to_json(self) -> dict:
        return {}

    @staticmethod
    def load_from_json(game_object: GameObject, params: dict) -> "PlayerController":
        return PlayerController(game_object)


def _get_direction(key: str) -> Vector3:
    match key:
        case "1":
            direction = Vector3(-1, -1, 0)
        case "2":
            direction = Vector3(0, -1, 0)
        case "3":
            direction = Vector3(1, -1, 0)
        case "6":
            direction = Vector3(1, 0, 0)
        case "9":
            direction = Vector3(1, 1, 0)
        case "8":
            direction = Vector3(0, 1, 0)
        case "7":
            direction = Vector3(-1, 1, 0)
        case "4":
            direction = Vector3(-1, 0, 0)
        case "+":
            direction = Vector3(0, 0, 1)
        case "-":
            direction = Vector3(0, 0, -1)
        case _:
            direction = Vector3(0, 0, 0)
    return direction
