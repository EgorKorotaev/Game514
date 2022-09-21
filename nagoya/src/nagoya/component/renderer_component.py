import numpy as np

from gif_maker.resources import load_sprites, GLOB_SPRITES
from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.object.game_object import GameObject
from nagoya.primitive.vector import Vector3
from nagoya.shader.shader import Shader

from .component import Component
from .component_visitor import ComponentVisitor
from ..sprite.sprite import Sprite


class RendererComponent(Component):
    def __init__(self, game_object: GameObject, shader: Shader, sprite: Sprite, priority: int):
        super().__init__(game_object)
        self._shader = shader
        self._sprite = sprite
        self.priority = priority  # TODO куда бы вынести и нужно-ли...

    @property
    def shader(self) -> Shader:
        return self._shader

    @property
    def sprite(self) -> np.ndarray:
        return self._sprite.get_sprite(glob_sprites=GLOB_SPRITES)

    def draw(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3) -> RenderedTile:
        return self._shader.render(underlying_tile, position_relative_to_camera)

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_renderer(self)

    def init(self) -> None:
        pass

    @staticmethod
    def create_renderer_component(game_object: GameObject, shader: Shader, sprite: Sprite) -> "RendererComponent":
        return RendererComponent(game_object=game_object, shader=shader, sprite=sprite, priority=0)
