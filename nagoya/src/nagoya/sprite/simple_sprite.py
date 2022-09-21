import numpy as np

from .sprite import Sprite
from .sprite_visitor import SpriteVisitor


class SimpleSprite(Sprite):
    def __init__(self, assets_folder: str, assets_file: str, assets_image: str):
        self.assets_folder = assets_folder
        self.assets_file = assets_file
        self.assets_image = assets_image

    def get_sprite(self, glob_sprites) -> np.ndarray:
        # TODO Срочно вынести
        default_sprite = np.array([[(0, 0, 0, 0) for x in range(24)] for y in range(24)])
        return glob_sprites.get(self.assets_folder, None).get(self.assets_file, None).get(self.assets_image, default_sprite)

    def accept(self, visitor: SpriteVisitor):
        return visitor.visit_simple(self)

    @staticmethod
    def create_simple_sprite(
        assets_folder: str = '',
        assets_file: str = '',
        assets_image: str = '',
    ) -> "SimpleSprite":
        return SimpleSprite(assets_folder, assets_file, assets_image)
