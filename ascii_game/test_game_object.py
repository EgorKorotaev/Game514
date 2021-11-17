from unittest import TestCase

from ascii_game.game_object import GameObject


class Test(TestCase):
    def test_game_object(self):
        # given
        test_game_object = GameObject(
            "0",
        )
        # when

        # then
