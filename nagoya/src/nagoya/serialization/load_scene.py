import json

from nagoya.object.game_object import GameObject
from nagoya.scene import Scene

from .load_component import load_component


def load_scene(scene_json: str) -> Scene:
    scene_raw = json.loads(scene_json)
    return _load_scene(scene_raw)


def _load_scene(scene_json: dict) -> Scene:
    return Scene(
        camera_id=scene_json["camera_id"],
        keyboard_subject_id=scene_json["keyboard_subject_id"],
        objects=[_load_game_object(game_object) for game_object in scene_json["objects"]],
    )


def _load_game_object(game_object: dict) -> GameObject:
    formed_game_object = GameObject()
    for component in game_object["components"]:
        formed_game_object.add_component(load_component(component=component, game_object=formed_game_object))
    return formed_game_object
