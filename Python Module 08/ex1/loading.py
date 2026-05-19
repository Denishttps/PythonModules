import importlib
from types import ModuleType
from typing import Optional


def import_module(name: str) -> Optional[ModuleType]:
    try:
        return importlib.import_module(name)
    except ImportError:
        return


def check_dependnsies():
    pandas = import_module("pandas")
    numpy = import_module("numpy")
    matplotlib = import_module("matplotlib")
    requests = import_module("requests")

    print(pandas)

check_dependnsies()