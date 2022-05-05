from nagoya.shader.shader import Shader
from nagoya.shader.simple_shader import SimpleShader
from nagoya.shader.simple_shader2 import SimpleShader2
from nagoya.shader.compromise_shader import CompromiseShader
from nagoya.shader.transparent_shader import TransparentShader

from .load_primitive import load_color_a, load_object_texture


def load_shader(shader: dict) -> Shader:
    match shader["type"]:
        case "SimpleShader":
            return _load_simple_shader(shader)
        case "SimpleShader2":
            return _load_simple_shader_2(shader)
        case "CompromiseShader":
            return _load_compromise_shader(shader)
        case "TransparentShader":
            return _load_transparent_shader(shader)


def _load_simple_shader(shader) -> SimpleShader:
    return SimpleShader(
        load_color_a(shader["background_color"]),
        load_color_a(shader["object_color"]),
        load_object_texture(shader["object_texture"]),
    )


def _load_simple_shader_2(shader) -> SimpleShader2:
    return SimpleShader2(
        load_color_a(shader["background_color"]),
        load_color_a(shader["object_color"]),
        load_object_texture(shader["object_texture"]),
    )


def _load_compromise_shader(shader) -> CompromiseShader:
    return CompromiseShader(
        load_color_a(shader["background_color"]),
        load_color_a(shader["object_color"]),
        load_object_texture(shader["object_texture"]),
    )


def _load_transparent_shader(shader) -> TransparentShader:
    return TransparentShader(load_color_a(shader["color"]))
