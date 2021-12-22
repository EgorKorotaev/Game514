from abc import ABC, abstractmethod
from typing import Any

from ascii_game.event_system.event_manager import EventManager
from ascii_game.visitor import ComponentVisitor


class Component(ABC):
    _event_manager = EventManager()

    def __init__(self, game_object: "GameObject"):
        self._game_object = game_object

    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def accept(self, visitor: ComponentVisitor) -> Any:
        pass

    def get_event_manager(self) -> EventManager:
        return Component._event_manager

    def this_game_object(self) -> "GameObject":
        return self._game_object
