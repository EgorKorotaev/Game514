from abc import ABC, abstractmethod


class ShaderVisitor(ABC):
    @abstractmethod
    def visit_simple(self, element: "SimpleShader"):
        pass

    @abstractmethod
    def visit_transparent(self, element: "TransparentShader"):
        pass
