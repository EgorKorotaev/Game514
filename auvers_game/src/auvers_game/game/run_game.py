import os

from bearlibterminal import terminal
from sty import bg, ef, fg, rs

from auvers_game.resources import resources_root, get_resource
from nagoya.component.camera_component import CameraComponent
from nagoya.component.keyboard_subject_component import KeyboardSubjectComponent
from nagoya.primitive.color_a import ColorA
from nagoya.render.bearlibterminal_renderer import render_to_terminal
from nagoya.render.renderer import render_scene
from nagoya.scene import Scene
from nagoya.serialization.load_scene import load_scene
from nagoya.serialization.serialize_scene import serialize_scene


def run_game():
    with open(get_resource("data.json") , "r") as json_scene:
        scene = load_scene(json_scene.read())
    game_loop(scene)


def game_loop(scene: Scene) -> None:
    terminal.open()
    terminal.set("font: D:\\Users\\Faunu\\PycharmProjects\\TestGame\\Symbola.ttf, size=50")
    # terminal.set("font: C:\\Windows\\Fonts\\seguisym.ttf, size=50")
    terminal.set(
        f"window: cellsize=64x64, size={scene.get_camera().get_component(CameraComponent).viewport.x}x{scene.get_camera().get_component(CameraComponent).viewport.y}"
    )

    while True:
        scene._objects[scene.keyboard_subject_id].get_component(KeyboardSubjectComponent).move(terminal.read())
        buffer = render_scene(scene)
        render_to_terminal(buffer)


def save_scene(scene):
    with open("data.json", "w") as f:
        f.write(serialize_scene(scene))
