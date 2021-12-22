from abc import ABC, abstractmethod


class ComponentVisitor(ABC):
    @abstractmethod
    def visit_camera(self, element: "CameraComponent"):
        pass

    @abstractmethod
    def visit_renderer(self, element: "RendererComponent"):
        pass

    @abstractmethod
    def visit_transform(self, element: "TransformComponent"):
        pass


class ShaderVisitor(ABC):
    @abstractmethod
    def visit_simple(self, element: "SimpleShader"):
        pass

    @abstractmethod
    def visit_transparent(self, element: "TransparentShader"):
        pass


class PrimitiveVisitor(ABC):
    @abstractmethod
    def visit_point(self, element: "Point"):
        pass

    @abstractmethod
    def visit_vector2(self, element: "Vector2"):
        pass

    @abstractmethod
    def visit_vector3(self, element: "Vector3"):
        pass

    @abstractmethod
    def visit_vector4(self, element: "Vector4"):
        pass

    @abstractmethod
    def visit_color_a(self, element: "ColorA"):
        pass
