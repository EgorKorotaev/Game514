from nagoya.shader.shader import Shader
from nagoya.shader.shader_visitor import ShaderVisitor
from nagoya.shader.simple_shader import SimpleShader
from nagoya.shader.compromise_shader import CompromiseShader
from nagoya.shader.transparent_shader import TransparentShader

from .serialize_primitive import serialize_color_a


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

    def visit_compromise(self, element: CompromiseShader) -> None:
        self.serialized_shader = {
            "type": "CompromiseShader",
            "background_color": serialize_color_a(element.background_color),
            "object_color": serialize_color_a(element.object_color),
            "object_texture": element.object_texture.object_id,
        }

    def visit_transparent(self, element: TransparentShader) -> None:
        self.serialized_shader = {"type": "TransparentShader", "color": serialize_color_a(element.color)}
