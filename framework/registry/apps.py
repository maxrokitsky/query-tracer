import importlib
import types
from dataclasses import dataclass
from typing import Self

from fastapi import APIRouter, FastAPI

from framework.db.base import BaseModel


@dataclass
class App:
    """App."""

    name: str
    models: dict[str, BaseModel]
    module: types.ModuleType
    routers: list[APIRouter]

    @classmethod
    def import_module(cls, name: str) -> Self:
        """Imports module by name."""
        module = importlib.import_module(f'{name}')

        return cls(
            name=name,
            models=cls._import_models(name),
            module=module,
            routers=cls._import_routers(name),
        )

    @staticmethod
    def _import_models(app_module: str) -> dict[str, BaseModel]:
        models_module = importlib.import_module(f'{app_module}.models')

        return {
            obj_name: obj
            for obj_name, obj in models_module.__dict__.items()
            if isinstance(obj, BaseModel)
        }

    @staticmethod
    def _import_routers(app_module: str) -> list[APIRouter]:
        try:
            router_module = importlib.import_module(f'{app_module}.api.router')
        except ImportError:
            router_module = importlib.import_module(f'{app_module}.api')
        return [
            obj for obj in router_module.__dict__.values() if isinstance(obj, APIRouter)
        ]


class AppRegistry:
    """App Registry."""

    apps: dict[str, App]

    def import_apps(self, names: list[str]) -> None:
        """Import and initialize installed apps."""
        self.apps = {name: App.import_module(name) for name in names}

    def inject_routers(self, fastapi_app: FastAPI) -> None:
        """Injects app routers in FastAPI app."""
        for app in self.apps.values():
            for router in app.routers:
                fastapi_app.include_router(router)


apps = AppRegistry()
