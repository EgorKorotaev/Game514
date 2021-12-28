from abc import ABC, abstractmethod


class ComponentVisitor(ABC):
    @abstractmethod
    def visit_camera(self, element: "CameraComponent") -> None:
        pass

    @abstractmethod
    def visit_keyboard_subject(self, element: "KeyboardSubjectComponent") -> None:
        pass

    @abstractmethod
    def visit_renderer(self, element: "RendererComponent") -> None:
        pass

    @abstractmethod
    def visit_transform(self, element: "TransformComponent") -> None:
        pass

    @abstractmethod
    def visit_player_controller(self, element: "PlayerController") -> None:
        pass
