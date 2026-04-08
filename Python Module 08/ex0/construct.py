import os
import sys
import site

from typing import Optional


_DEFAULT = "\033[{code}m"
_RESET_COLOR = _DEFAULT.format(code=0)
_RGB = "{};2;{};{};{}"


def _validate_rgb(r: int, g: int, b: int):
    for value in (r, g, b):
        if not (0 <= value <= 255):
            raise ValueError("RGB values must be in range 0–255")


def rgb(
        r: int,
        g: int,
        b: int,
        text: Optional[str] = None,
        background: bool = False
) -> str:
    _validate_rgb(r, g, b)
    mode = 48 if background else 38
    color = _DEFAULT.format(code=_RGB.format(mode, r, g, b))
    if text is not None:
        return f"{color}{text}{_RESET_COLOR}"
    return color


def in_venv() -> None:
    user_site_packages = site.getusersitepackages()
    print(
        f"Environment Path: {os.getenv('VIRTUAL_ENV')}",
        "",
        f"{rgb(0, 255, 0, 'SUCCESS')}:  You're in an isolated environment!",
        "Safe to install packages without affecting the global system.",
        "",
        f"Package installation path: {rgb(0, 100, 255, user_site_packages)}",
        sep="\n"
    )


def notify_global_usage() -> None:
    print(
        "",
        f"{rgb(255, 255, 0, 'WARNING')}: You're in the global environment!",
        "The machines can see everything you install",
        "",
        "To enter the construct, run:",
        rgb(0, 255, 255, "python -m venv matrix_env"),
        rgb(0, 255, 255, "source matrix_env/bin/activate ") + "# On Unix",
        rgb(0, 255, 255, "matrix_venv/Scripts/activate ") + "# On Windows",
        "",
        "Then run this program again.",
        sep="\n"
    )


def main():
    print(f"{rgb(255, 100, 100, 'MATRIX STATUS')}: You're still plugged in")

    print()

    is_venv = sys.prefix != sys.base_prefix
    venv_name = os.getenv("VIRTUAL_ENV")
    if venv_name:
        venv_name = venv_name.split("/")[-1]

    print(f"Current Python: {rgb(0, 100, 255, sys.executable)}")
    print(f"Virtual Environment: {venv_name if is_venv else 'None detected'}")

    if is_venv:
        in_venv()
    else:
        notify_global_usage()


if __name__ == "__main__":
    main()
