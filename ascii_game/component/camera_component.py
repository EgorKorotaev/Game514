from ascii_game.component.component import Component
from ascii_game.object.game_object import GameObject
from ascii_game.visitor import ComponentVisitor
from ascii_game.primitive.color_a import ColorA
from ascii_game.shader.shader import Shader
from ascii_game.shader.simple_shader import SimpleShader
from ascii_game.render.texture import ObjectTexture
from ascii_game.primitive.vector import Vector3


class CameraComponent(Component):
    def __init__(self, game_object: GameObject, viewport: Vector3, default_rendered_shader: Shader):
        super().__init__(game_object)
        self.viewport = viewport
        self.default_rendered_shader = default_rendered_shader

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_camera(self)

    def init(self) -> None:
        pass

    @staticmethod
    def create_camera_component(game_object: GameObject) -> "CameraComponent":
        return CameraComponent(
            game_object=game_object,
            viewport=Vector3(8, 8, 8),
            default_rendered_shader=SimpleShader.create_simple_shader(),
        )
