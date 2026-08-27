import os
from pathlib import Path

from app.config import settings

DEFAULT_INFORMES_PATH_FILE = settings.BASE_DIR / "default_informes_path.txt"


def save_default_folder_path(path: str | None) -> None:
    if not path:
        return

    try:
        DEFAULT_INFORMES_PATH_FILE.write_text(path, encoding="utf-8")
    except OSError:
        pass


def load_default_folder_path() -> str | None:
    if not DEFAULT_INFORMES_PATH_FILE.exists():
        return None

    try:
        path = DEFAULT_INFORMES_PATH_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return None

    return path or None
