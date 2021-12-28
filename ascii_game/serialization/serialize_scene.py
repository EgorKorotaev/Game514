import json

from ascii_game.object.game_object import GameObject
from ascii_game.scene import Scene
from ascii_game.serialization.serialize_component import serialize_component


def serialize_scene(scene: Scene) -> str:
    scene_json = _serialize_scene(scene)
    return json.dumps(scene_json)


def _serialize_scene(scene: Scene) -> dict:
    return {
        "objects": [_serialize_game_object(game_object) for game_object in scene.game_objects()],
        "camera_id": scene.camera_id,
        "keyboard_subject_id": scene.keyboard_subject_id,
    }


def _serialize_game_object(game_object: GameObject) -> dict:
    return {"components": [serialize_component(game_object._components[key]) for key in game_object._components.keys()]}
