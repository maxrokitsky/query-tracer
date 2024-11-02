from typing import ClassVar

from pydantic_settings import BaseSettings as PydanticSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticSettings):
    """Project settings."""

    db_url: str
    apps: ClassVar[list[str]]

    model_config = SettingsConfigDict(
        env_prefix='framework_',
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


def init_settings(settings_class: type[BaseSettings]) -> BaseSettings:
    """Initialize settings."""
    return settings_class()  # pyright: ignore [reportCallIssue]
