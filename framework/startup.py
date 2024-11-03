import importlib
import os

from .registry import apps


def startup() -> None:
    """Project setup."""
    settings_module = importlib.import_module(os.environ['SETTINGS_MODULE'])
    settings = settings_module.settings
    apps.import_apps(settings.apps)
