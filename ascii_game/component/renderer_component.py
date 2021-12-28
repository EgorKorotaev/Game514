from ascii_game.component.component import Component
from ascii_game.drawing_in_console.rendered_tile import RenderedTile
from ascii_game.object.game_object import GameObject
from ascii_game.visitor import ComponentVisitor
from ascii_game.shader.shader import Shader
from ascii_game.primitive.vector import Vector3


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
