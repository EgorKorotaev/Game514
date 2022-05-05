from abc import ABC, abstractmethod


class ShaderVisitor(ABC):
    @abstractmethod
    def visit_simple(self, element: "SimpleShader"):
        pass

    def visit_simple2(self, element: "SimpleShader2"):
        pass

    @abstractmethod
    def visit_compromise(self, element: "CompromiseShader"):
        pass

    @abstractmethod
    def visit_transparent(self, element: "TransparentShader"):
        pass
