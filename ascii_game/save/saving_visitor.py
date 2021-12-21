from dataclasses import dataclass

from ascii_game.component.camera_component import CameraComponent
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.component.transform_component import TransformComponent
from ascii_game.visitor import ComponentVisitor, ShaderVisitor, PrimitiveVisitor
from ascii_game.primitive.color_a import ColorA
from ascii_game.shader.simple_shader import SimpleShader
from ascii_game.shader.transparent_shader import TransparentShader
from ascii_game.primitive.vector import Point, Vector2, Vector3, Vector4


class JSONExportPrimitiveVisitor(PrimitiveVisitor):

    def visit_point(self, element: Point):
        data = {
            'type': 'Point',
            'field': [
                {
                    'name': 'x',
                    'value': element.x
                }
            ]
        }
        return data

    def visit_vector2(self, element: Vector2):
        data = {
            'type': 'Vector2',
            'field': [
                {
                    'name': 'x',
                    'value': element.x
                },
                {
                    'name': 'y',
                    'value': element.y
                }
            ]
        }
        return data

    def visit_vector3(self, element: Vector3):
        data = {
            'type': 'Vector3',
            'field': [
                {
                    'name': 'x',
                    'value': element.x
                },
                {
                    'name': 'y',
                    'value': element.y
                },
                {
                    'name': 'z',
                    'value': element.z
                }
            ]
        }
        return data

    def visit_vector4(self, element: Vector4):
        data = {
            'type': 'Vector4',
            'field': [
                {
                    'name': 'x',
                    'value': element.x
                },
                {
                    'name': 'y',
                    'value': element.y
                },
                {
                    'name': 'z',
                    'value': element.z
                },
                {
                    'name': 'w',
                    'value': element.w
                }
            ]
        }
        return data

    def visit_color_a(self, element: ColorA):
        data = {
            'type': 'ColorA',
            'field': [
                {
                    'name': 'r',
                    'value': element.r
                },
                {
                    'name': 'g',
                    'value': element.g
                },
                {
                    'name': 'b',
                    'value': element.b
                },
                {
                    'name': 'a',
                    'value': element.a
                }
            ]
        }
        return data


class JSONExportShaderVisitor(ShaderVisitor):
    json_export_primitive_visitor = JSONExportPrimitiveVisitor()

    def visit_simple(self, element: SimpleShader):
        data = {
            'type': 'SimpleShader',
            'field': [
                {
                    'name': 'background_color',
                    'value': element.background_color.accept(self.json_export_primitive_visitor)
                },
                {
                    'name': 'object_color',
                    'value': element.object_color.accept(self.json_export_primitive_visitor)
                },
                {
                    'name': 'object_texture',
                    'value': {
                        'type': 'ObjectTexture',
                        'field': [
                            {
                                'name': 'object_id',
                                'value': element.object_texture.object_id
                            }
                        ]
                    }
                }
            ]
        }
        return data

    def visit_transparent(self, element: TransparentShader):
        data = {
            'type': 'SimpleShader',
            'field': [
                {
                    'name': 'color',
                    'value': element.color.accept(self.json_export_primitive_visitor)
                }
            ]
        }
        return data


@dataclass
class JSONExportComponentVisitor(ComponentVisitor):
    json_export_primitive_visitor = JSONExportPrimitiveVisitor()
    json_export_shader_visitor = JSONExportShaderVisitor()

    def visit_camera(self, element: CameraComponent):
        data = {
            'type': 'CameraComponent',
            'field': [
                {
                    'name': 'viewport',
                    'value': element.viewport.accept(self.json_export_primitive_visitor)
                },
                {
                    'name': 'default_rendered_shader',
                    'value': element.default_rendered_shader.accept(self.json_export_shader_visitor)
                }
            ]
        }
        return data

    def visit_renderer(self, element: RendererComponent):
        data = {
            'type': 'RendererComponent',
            'field': [
                {
                    'name': 'shader',
                    'value': element.shader.accept(self.json_export_shader_visitor)
                },
                {
                    'name': 'priority',
                    'value': element.priority
                }
            ]
        }
        return data

    def visit_transform(self, element: TransformComponent):
        data = {
            'type': 'TransformComponent',
            'field': [
                {
                    'name': 'position',
                    'value': element.position.accept(self.json_export_primitive_visitor)
                }
            ]
        }
        return data
