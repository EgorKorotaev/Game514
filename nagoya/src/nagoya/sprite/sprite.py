import numpy as np
from abc import ABC, abstractmethod

from nagoya.sprite.sprite_visitor import SpriteVisitor


class Sprite(ABC):
    @abstractmethod
    def get_sprite(self, glob_sprites: dict) -> np.ndarray:
        pass

    @abstractmethod
    def accept(self, visitor: SpriteVisitor):
        pass
