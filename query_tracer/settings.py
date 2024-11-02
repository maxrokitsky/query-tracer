from typing import ClassVar

from framework.configuration.base import BaseSettings, init_settings


class Settings(BaseSettings):
    """Project settings."""

    apps: ClassVar[list[str]] = [
        'query_tracer.request',
    ]


settings = init_settings(Settings)
