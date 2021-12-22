from dataclasses import dataclass
from typing import Any

from ascii_game.component.component import Component
from ascii_game.event_system.event_manager import Event
from ascii_game.object.game_object import GameObject
from ascii_game.visitor import ComponentVisitor


class KeyboardEvent(Event):
    def __init__(self, key: str):
        self._key = key

    @staticmethod
    def name() -> str:
        return "KeyboardEvent"

    def payload(self) -> Any:
        return self._key


class KeyboardSubjectComponent(Component):
    def init(self) -> None:
        pass

    def move(self):
        event_manager = self.get_event_manager()
        keyboard_input = input()
        match keyboard_input:
            case "1":
                event_manager.notify(KeyboardEvent("1"))
            case "2":
                event_manager.notify(KeyboardEvent("2"))
            case "3":
                event_manager.notify(KeyboardEvent("3"))
            case "6":
                event_manager.notify(KeyboardEvent("6"))
            case "9":
                event_manager.notify(KeyboardEvent("9"))
            case "8":
                event_manager.notify(KeyboardEvent("8"))
            case "7":
                event_manager.notify(KeyboardEvent("7"))
            case "4":
                event_manager.notify(KeyboardEvent("4"))

    def accept(self, visitor: ComponentVisitor) -> None:
        pass


def create_keyboard_subject():
    keyboard_subject = GameObject.create_game_object()
    keyboard_subject.add_component(KeyboardSubjectComponent(keyboard_subject))
    return keyboard_subject


# match keyboard_input:
#             case "1":
#                 event_manager.notify(KeyboardEvent('1')
#             case "2":
#                 event_manager.notify(KeyboardEvent('1')
#             case "3":
#                 event_manager.notify(KeyboardEvent('1')
#             case "6":
#                 event_manager.notify(KeyboardEvent('1')
#             case "9":
#                 event_manager.notify(KeyboardEvent('1')
#             case "8":
#                 event_manager.notify(KeyboardEvent('1')
#             case "7":
#                 event_manager.notify(KeyboardEvent('1')
#             case "4":
#                 event_manager.notify(KeyboardEvent('1')
