from abc import ABC, abstractmethod


class SpriteVisitor(ABC):
    @abstractmethod
    def visit_simple(self, element: "SimpleSprite"):
        pass
