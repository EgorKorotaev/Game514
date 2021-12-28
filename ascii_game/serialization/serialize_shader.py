from ascii_game.serialization.serialize_primitive import serialize_color_a
from ascii_game.shader.shader import Shader
from ascii_game.shader.simple_shader import SimpleShader
from ascii_game.shader.transparent_shader import TransparentShader
from ascii_game.visitor import ShaderVisitor


def serialize_shader(shader: Shader) -> dict:
    json_shader_visitor = JSONExportShaderVisitor()
    shader.accept(json_shader_visitor)
    return json_shader_visitor.serialized_shader


class JSONExportShaderVisitor(ShaderVisitor):
    def __init__(self):
        self.serialized_shader: dict = {}

    def visit_simple(self, element: SimpleShader) -> None:
        self.serialized_shader = {
            "type": "SimpleShader",
            "background_color": serialize_color_a(element.background_color),
            "object_color": serialize_color_a(element.object_color),
            "object_texture": element.object_texture.object_id,
        }

    def visit_transparent(self, element: TransparentShader) -> None:
        self.serialized_shader = {"type": "TransparentShader", "color": serialize_color_a(element.color)}
