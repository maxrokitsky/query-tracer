import importlib
import os

settings_module = importlib.import_module(os.environ['SETTINGS_MODULE'])

apps = settings_module.settings.apps


def startup() -> None:
    """Project setup."""
    for app in apps:
        importlib.import_module(f'{app}.models')
        # if getattr(module, "recursive", None):
