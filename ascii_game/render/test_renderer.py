from unittest import TestCase

from ascii_game.component.renderer_component import RendererComponent
from ascii_game.object.game_object import GameObject
from ascii_game.render.camera import create_camera
from ascii_game.render.color_a import ColorA
from ascii_game.render.renderer import Buffer
from ascii_game.render.shader import RenderedTile, DefaultShader
from ascii_game.render.texture import BackgroundColor, ObjectColor, ObjectTexture
from ascii_game.vector import Vector3


class TestBuffer(TestCase):
    def test_draw_tile_add_game_object_1_1(self):
        # given
        camera = create_camera()
        camera.transform.position = Vector3(4, 6, 5)
        buffer = Buffer(camera=camera)

        background_color = BackgroundColor(ColorA(a=0))
        object_color = ObjectColor(ColorA(a=0))
        object_texture = ObjectTexture(object_id="no default")

        game_object = GameObject()
        game_object.transform.position = Vector3(5, 7, 6)
        game_object.add_component(RendererComponent(DefaultShader(background_color, object_color, object_texture)))

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

        game_object = GameObject()
        game_object.transform.position = Vector3(1, 1, 2)
        game_object.add_component(RendererComponent(DefaultShader(background_color, object_color, object_texture)))

        shader = DefaultShader()
        default_rendered_tile = shader.render(underlying_tile=None, position_z=0)

        # when
        buffer.add_game_object(game_object=game_object)
        buffer.draw_tiles()

        # then
        self.assertEqual(
            [[default_rendered_tile for x in range(camera.viewport.x)] for y in range(camera.viewport.y)],
            buffer.rendered_tiles,
        )
