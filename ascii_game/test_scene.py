from unittest import TestCase

from ascii_game.render.camera import Camera
from ascii_game.scene import Scene


class TestScene(TestCase):
    def test_get_camera_camera_id_correct(self):
        # given
        scene = Scene()

        # when
        camera = scene.get_camera()

        # then
        self.assertEqual(type(camera), Camera)
