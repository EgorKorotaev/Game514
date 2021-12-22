from abc import ABC, abstractmethod
from typing import Any

from ascii_game.visitor import ComponentVisitor


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: ComponentVisitor) -> Any:
        pass

    @abstractmethod
    def update(self, subject) -> None:
        pass
