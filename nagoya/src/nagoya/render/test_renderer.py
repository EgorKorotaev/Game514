from unittest import TestCase

from nagoya.component.renderer_component import RendererComponent
from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.object.game_object import GameObject
from nagoya.primitive import ColorA
from nagoya.primitive.vector import Vector3
from nagoya.render.camera import create_camera
from nagoya.shader.transparent_shader import TransparentShader

from .renderer import Buffer
from .texture import BackgroundColor, ObjectColor, ObjectTexture


class TestBuffer(TestCase):
    def test_draw_tile_add_game_object_1_1(self):
        # given
        camera = create_camera()
        camera.transform.position = Vector3(4, 6, 5)
        buffer = Buffer(camera=camera)

        background_color = BackgroundColor(ColorA(a=0))
        object_color = ObjectColor(ColorA(a=0))
        object_texture = ObjectTexture(object_id="no default")

        game_object = GameObject.create_game_object()
        game_object.transform.position = Vector3(5, 7, 6)
        game_object.add_component(
            RendererComponent.create_renderer_component(
                TransparentShader(background_color, object_color, object_texture)
            )
        )

        rendered_tile = RenderedTile(background_color, object_color, object_texture)

        # when
        buffer.add_game_object(game_object=game_object)
        buffer.draw_tiles()

        # then
        self.assertEqual(rendered_tile, buffer.rendered_tiles[1][1])

    def test_draw_tile_add_game_object_out_of_range(self):
        # given
        camera = create_camera()
        camera.transform.position = Vector3()
        camera.viewport = Vector3(1, 1, 1)
        buffer = Buffer(camera=camera)

        background_color = BackgroundColor(ColorA(a=0))
        object_color = ObjectColor(ColorA(a=0))
        object_texture = ObjectTexture(object_id="no default")

        game_object = GameObject.create_game_object()
        game_object.transform.position = Vector3(1, 1, 2)
        game_object.add_component(
            RendererComponent.create_renderer_component(
                TransparentShader(background_color, object_color, object_texture)
            )
        )

        shader = TransparentShader()
        default_rendered_tile = shader.render(underlying_tile=None, position_z=0)

        # when
        buffer.add_game_object(game_object=game_object)
        buffer.draw_tiles()

        # then
        self.assertEqual(
            [[default_rendered_tile for x in range(camera.viewport.x)] for y in range(camera.viewport.y)],
            buffer.rendered_tiles,
        )
