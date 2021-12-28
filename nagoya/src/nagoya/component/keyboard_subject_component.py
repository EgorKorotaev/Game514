from typing import Any

from bearlibterminal import terminal

from nagoya.event_system.event_manager import Event
from nagoya.object.game_object import GameObject

from .component import Component
from .component_visitor import ComponentVisitor


def create_keyboard_subject():
    keyboard_subject = GameObject.create_game_object()
    keyboard_subject.add_component(KeyboardSubjectComponent.create_keyboard_subject_component(keyboard_subject))
    return keyboard_subject


class KeyboardSubjectComponent(Component):
    def __init__(self, game_object: GameObject):
        super().__init__(game_object)

    def move(self, keyboard_input):
        event_manager = self.get_event_manager()
        match keyboard_input:
            case "1" | terminal.TK_KP_1:
                event_manager.notify(KeyboardEvent("1"))
            case "2" | terminal.TK_KP_2:
                event_manager.notify(KeyboardEvent("2"))
            case "3" | terminal.TK_KP_3:
                event_manager.notify(KeyboardEvent("3"))
            case "6" | terminal.TK_KP_6:
                event_manager.notify(KeyboardEvent("6"))
            case "9" | terminal.TK_KP_9:
                event_manager.notify(KeyboardEvent("9"))
            case "8" | terminal.TK_KP_8:
                event_manager.notify(KeyboardEvent("8"))
            case "7" | terminal.TK_KP_7:
                event_manager.notify(KeyboardEvent("7"))
            case "4" | terminal.TK_KP_4:
                event_manager.notify(KeyboardEvent("4"))

    def accept(self, visitor: ComponentVisitor) -> None:
        return visitor.visit_keyboard_subject(self)

    def init(self) -> None:
        pass

    @staticmethod
    def create_keyboard_subject_component(game_object: GameObject) -> "KeyboardSubjectComponent":
        return KeyboardSubjectComponent(game_object=game_object)


class KeyboardEvent(Event):
    def __init__(self, key: str):
        self._key = key

    @staticmethod
    def name() -> str:
        return "KeyboardEvent"

    def payload(self) -> Any:
        return self._key
