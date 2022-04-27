from bearlibterminal import terminal

from auvers_game.resources import get_resource
from generator.main import generation_map
from nagoya.component.camera_component import CameraComponent
from nagoya.component.keyboard_subject_component import KeyboardSubjectComponent
from nagoya.render.bearlibterminal_renderer import render_to_terminal
from nagoya.render.renderer import render_scene
from nagoya.scene import Scene
from nagoya.serialization.load_scene import load_scene
from nagoya.serialization.serialize_scene import serialize_scene


def run_game():
    scene = load_scene(generation_map())
    game_loop(scene)


def game_loop(scene: Scene) -> None:
    size = 16
    terminal.open()
    font_path = get_resource("Symbola.ttf")
    terminal.set(f"font: {font_path}, size={size}")
    terminal.set(
        f"window: cellsize={size}x{size}, size={scene.get_camera().get_component(CameraComponent).viewport.x}x{scene.get_camera().get_component(CameraComponent).viewport.y}"
    )

    while True:
        if terminal.has_input():
            scene._objects[scene.keyboard_subject_id].get_component(KeyboardSubjectComponent).move(terminal.read())
        buffer = render_scene(scene)
        render_to_terminal(buffer)


def save_scene(scene):
    with open("data.json", "w") as f:
        f.write(serialize_scene(scene))
