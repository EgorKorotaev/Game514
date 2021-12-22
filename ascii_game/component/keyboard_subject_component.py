import time
from dataclasses import dataclass, field
from threading import Thread

import keyboard

from ascii_game.component.component import Component
from ascii_game.object.game_object import GameObject
from ascii_game.primitive.vector import Vector3
from ascii_game.visitor import ComponentVisitor


@dataclass
class EventManager:
    _observers: dict[str, list[Component]] = field(default_factory=dict)

    def attach(self, eventType: str, observer: Component) -> None:  # TODO сделать что-то с "eventType"
        if eventType in self._observers:
            self._observers[eventType].append(observer)
        else:
            self._observers[eventType] = [observer]

    def detach(self, eventType: str, observer: Component) -> None:
        self._observers[eventType].remove(observer)

    def notify(self, eventType: str, data) -> None:  # TODO сделать что-то с "data"
        for observer in self._observers[eventType]:
            observer.update(data)


@dataclass
class KeyboardSubjectComponent(Component):
    event_manager: EventManager = EventManager()

    def __init__(self):
        self.event_manager = EventManager()

    def move(self):
        x = input()
        data_click = f"up.{x}"
        if data_click == "up.1":
            self.event_manager.notify(data_click, Vector3(-1, 1, 0))
        if data_click == "up.2":
            self.event_manager.notify(data_click, Vector3(0, 1, 0))
        if data_click == "up.3":
            self.event_manager.notify(data_click, Vector3(1, 1, 0))
        if data_click == "up.6":
            self.event_manager.notify(data_click, Vector3(1, 0, 0))
        if data_click == "up.9":
            self.event_manager.notify(data_click, Vector3(1, -1, 0))
        if data_click == "up.8":
            self.event_manager.notify(data_click, Vector3(0, -1, 0))
        if data_click == "up.7":
            self.event_manager.notify(data_click, Vector3(-1, -1, 0))
        if data_click == "up.4":
            self.event_manager.notify(data_click, Vector3(-1, 0, 0))

    def update(self, subject) -> None:
        pass

    def accept(self, visitor: ComponentVisitor) -> None:
        pass


def create_keyboard_subject():
    keyboard_subject = GameObject.create_game_object()
    keyboard_subject.add_component(KeyboardSubjectComponent())
    return keyboard_subject
