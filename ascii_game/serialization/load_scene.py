import json

from ascii_game.object.game_object import GameObject
from ascii_game.scene import Scene


def load_scene(scene_json: str) -> Scene:
    scene_raw = json.loads(scene_json)
    return _load_scene(scene_raw)


def _load_game_object(game_object: dict) -> GameObject:
    return GameObject(
        transform=serialize_component(game_object.transform),
        components=[serialize_component(game_object._components[key]) for key in game_object._components.keys()],
    )


def _load_scene(scene_json: dict) -> Scene:
    return Scene(
        camera_id=scene_json["camera_id"],
        keyboard_subject_id=scene_json["keyboard_subject_id"],
        objects=[_load_game_object(game_object) for game_object in scene_json["objects"]],
    )
