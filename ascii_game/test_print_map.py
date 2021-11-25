from copy import deepcopy

from ascii_game.object.game_objects_prefab import GameObjectsPrefab, get_game_object
from ascii_game.render.camera import Camera
from ascii_game.render.colored_text import colored_background, ANSIColor
from ascii_game.render.renderer import render_scene
from ascii_game.scene import Scene
from ascii_game.vector import Vector3


def main():
    scene = Scene()
    for y in range(9):
        for x in range(9):
            wheat = deepcopy(get_game_object(GameObjectsPrefab.WHEAT))
            wheat.transform.position = Vector3(x, y, 3)
            scene.add_object(wheat)

            field = deepcopy(get_game_object(GameObjectsPrefab.FIELD))
            field.transform.position = Vector3(x, y, 2)
            scene.add_object(field)

    player = deepcopy(get_game_object(GameObjectsPrefab.PLAYER))

    player.transform.position = Vector3(1, 1, 3)

    scene.add_object(player)

    # print(colored_background('***', ANSIColor.RED))

    buffer = render_scene(scene)
    buffer.print()


if __name__ == "__main__":
    main()
