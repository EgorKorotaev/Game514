import time
from datetime import datetime

from bearlibterminal import terminal

from auvers_game.resources import get_resource
from map_generator.main import generation_map
from nagoya.component.camera_component import CameraComponent
from nagoya.component.keyboard_subject_component import KeyboardSubjectComponent
from nagoya.render.bearlibterminal_renderer import render_to_terminal
from nagoya.render.renderer import render_scene
from nagoya.render.renderer2 import render_scene2
from nagoya.scene import Scene
from nagoya.serialization.load_scene import load_scene
from nagoya.serialization.serialize_scene import serialize_scene


def run_game():
    seed = datetime.today().strftime("%Y_%m_%d-%H_%M_%S")
    print(seed)
    scene = load_scene(generation_map(seed="2022_05_04-23_15_07", max_height=8, map_size=64, viewport_size=32))
    # scene = load_scene(generation_map(seed=seed, map_size=32, viewport_size=64))
    game_loop(scene)


def game_loop(scene: Scene) -> None:
    size = 16
    terminal.open()
    font_path = get_resource("Symbola.ttf")
    terminal.set(f"font: {font_path}, size={int(size * 1.3)}")

    cam_viewport_y = scene.get_camera().get_component(CameraComponent).viewport.y
    cam_viewport_x = scene.get_camera().get_component(CameraComponent).viewport.x
    cam_viewport_z = scene.get_camera().get_component(CameraComponent).viewport.z
    size_x = cam_viewport_x * 2 + cam_viewport_y + 3
    size_y = cam_viewport_y + cam_viewport_z + 3

    terminal.set(
        f"window: cellsize={size}x{size}, size={size_x}x{size_y}"
    )

    while True:
        if terminal.has_input():
            scene._objects[scene.keyboard_subject_id].get_component(KeyboardSubjectComponent).move(terminal.read())
        buffer = render_scene2(scene)
        render_to_terminal(buffer)


def save_scene(scene):
    with open("data.json", "w") as f:
        f.write(serialize_scene(scene))
