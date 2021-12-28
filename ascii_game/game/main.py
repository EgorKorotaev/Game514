from bearlibterminal import terminal
from sty import fg, bg, ef, rs

from ascii_game.component.camera_component import CameraComponent
from ascii_game.component.keyboard_subject_component import KeyboardSubjectComponent
from ascii_game.primitive.color_a import ColorA
from ascii_game.render.bearlibterminal_renderer import render_to_terminal
from ascii_game.render.renderer import render_scene
from ascii_game.scene import Scene
from ascii_game.serialization.load_scene import load_scene
from ascii_game.serialization.serialize_scene import serialize_scene


def main():
    with open("data.json", "r") as json_scene:
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


def test_color():
    def colors_16(color_):
        # return "\033[2;{num}m {num} \033[0;0m".format(num=str(color_ + 10))
        return "\033[2;{num}m {num} \033[0;0m".format(num=str(color_ + 10))

    def colors_256(color_, len=16):
        num1 = str(color_ + 1)
        num2 = str(color_).ljust(5, " ")
        num2 = "▩"
        num2 = "🪶"
        num2 = "👻"

        end_symbol = ""
        if color_ % len + 2 == len - 1:
            end_symbol = "\n"

        # return f"\033[38;5;{num1}m{num2}\033[0;0m{end_symbol}"
        return f"{ef.blink}{fg(color_)}{num2}{rs.all}{end_symbol}"

    print("The 16 colors scheme is:")
    # print(" ".join([colors_16(x) for x in range(30, 38)]))
    print(f"{fg.black}👻{fg.rs}")
    print(f"{fg.da_grey}👻{fg.rs}")
    print(f"{fg.grey}👻{fg.rs}")
    print(f"{fg.li_grey}👻{fg.rs}")
    print(f"{fg.li_grey}👻{fg.rs}\n")

    print("\nThe 256 colors scheme is:")
    print("".join([colors_256(x) for x in range(16)]))
    print("".join([colors_256(x, 6) for x in range(16, 232)]))
    print("".join([colors_256(x) for x in range(232, 256)]))


def test_color2():
    color_b = ColorA()

    color_red = ColorA()
    color_red.set_rgb(1, 0, 0)
    color_red.a = 0.3

    color_blue = ColorA()
    color_blue.set_rgb(0, 0, 1)
    color_blue.a = 0.7

    color_dark = ColorA(1, 1, 1, 0.5)
    # color_dark.set_hsl(0, 0.8, 0.90)
    # color_dark.a = 0.9

    color_result = color_red + color_dark
    color_result_1 = color_red + color_blue
    color_result_2 = color_blue + color_red

    r, g, b = (color_b + color_red).get_rgb()
    print(f"{bg(r, g, b)}{color_red.a}{rs.all}")

    r, g, b = (color_b + color_red + color_dark).get_rgb()
    print(f"{bg(r, g, b)}{color_result.a}{rs.all}")

    r, g, b = color_result_1.get_rgb()
    print(f"{bg(r, g, b)}{color_result_1.a}{rs.all}")

    r, g, b = color_result_2.get_rgb()
    print(f"{bg(r, g, b)}{color_result_2.a}{rs.all}")
