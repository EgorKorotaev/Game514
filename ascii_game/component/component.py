from abc import ABC, abstractmethod

from ascii_game.visitor import ComponentVisitor


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: ComponentVisitor) -> None:
        pass
