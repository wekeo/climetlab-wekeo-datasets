import os

from .utils import hda2cml


def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "version")
    with open(version_file, "r") as f:
        version = f.readlines()
        version = version[0]
        version = version.strip()
    return version


__version__ = get_version()

__all__ = [
    "__version__",
    "hda2cml",
]
