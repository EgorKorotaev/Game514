from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.object.game_object import GameObject
from nagoya.primitive.vector import Vector3
from nagoya.shader.shader import Shader

from .component import Component
from .component_visitor import ComponentVisitor


class RendererComponent(Component):
    def __init__(self, game_object: GameObject, shader: Shader, priority: int):
        super().__init__(game_object)
        self._shader = shader
        self.priority = priority  # TODO куда бы вынести и нужно-ли...

    @property
    def shader(self) -> Shader:
        return self._shader

    def draw(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3) -> RenderedTile:
        return self._shader.render(underlying_tile, position_relative_to_camera)

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_renderer(self)

    def init(self) -> None:
        pass

    @staticmethod
    def create_renderer_component(game_object: GameObject, shader: Shader) -> "RendererComponent":
        return RendererComponent(game_object=game_object, shader=shader, priority=0)
