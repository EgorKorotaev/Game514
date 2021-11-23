from unittest import TestCase

from ascii_game.object.game_object import GameObject
from ascii_game.render.camera import Camera
from ascii_game.render.renderer import Buffer
from ascii_game.render.shader import RenderedTile
from ascii_game.render.texture import BackgroundTexture, ObjectTexture
from ascii_game.vector import Vector3, Vector2


class TestBuffer(TestCase):
    def test_draw_tile(self):
        # given
        camera = Camera(Vector2(2, 2))
        camera.transform.position = Vector3(4, 6, 7)
        buffer = Buffer(camera=camera)

        game_object = GameObject()
        game_object.transform.position = Vector3(5, 7, 6)

        rendered_tile = RenderedTile(BackgroundTexture(), ObjectTexture())

        # when
        buffer.draw_tile(game_object=game_object)

        # then
        self.assertEqual(rendered_tile, buffer.tiles[1][1])
