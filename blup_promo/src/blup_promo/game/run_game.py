import keyboard as keyboard

from map_generator.main import generation_map
from nagoya.component import KeyboardSubjectComponent
from nagoya.render.terminal_renderer import render_to_terminal
from nagoya.render.renderer import render_scene
from nagoya.scene import Scene
from nagoya.serialization.load_scene import load_scene
from nagoya.serialization.serialize_scene import serialize_scene


def run_game():
    scene = load_scene(generation_map())
    game_loop(scene)


def game_loop(scene: Scene) -> None:
    def print_pressed_keys(e):
        if e.event_type != "down":
            return
        e_ = e.name
        match e_:
            case "1":
                e_ = "7"
            case "2":
                e_ = "8"
            case "3":
                e_ = "9"
            case "9":
                e_ = "3"
            case "8":
                e_ = "2"
            case "7":
                e_ = "1"
            case "4":
                e_ = "4"
            case "6":
                e_ = "6"
            case "+":
                e_ = "+"
            case "-":
                e_ = "-"
        scene._objects[scene.keyboard_subject_id].get_component(KeyboardSubjectComponent).move(e_)
        buffer = render_scene(scene)
        render_to_terminal(buffer)

    while True:
        keyboard.hook(print_pressed_keys)
        keyboard.wait()


def save_scene(scene):
    with open("data.json", "w") as f:
        f.write(serialize_scene(scene))
