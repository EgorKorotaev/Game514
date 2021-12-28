import os


def resources_root() -> str:
    return os.path.join(os.path.dirname(__file__), os.path.pardir, "resources")

def get_resource(resource_name: str) -> str:
    return os.path.join(resources_root(), resource_name)