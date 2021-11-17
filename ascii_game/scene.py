from dataclasses import dataclass

from ascii_game.game_object import GameObject


@dataclass
class Scene:
    objects: list[GameObject]

    def __init__(self):
        self.objects = []

    def add_object(self, game_object: GameObject):
        self.objects.append(game_object)
