import datetime
from typing import Any, TypedDict

from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from framework.db import Model
from query_tracer.request.models.request import Request


class TracebackFrame(TypedDict):
    """Traceback Frame."""

    filename: str
    line: int
    function: str
    code: list[str]
    range: tuple[int, int]


class Query(Model):
    """Query Model."""

    __tablename__ = 'queries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    sql: Mapped[str]
    params: Mapped[list[Any]] = mapped_column(JSON())
    timestamp: Mapped[datetime.datetime]
    duration: Mapped[float]
    traceback: Mapped[list[TracebackFrame]] = mapped_column(JSON())
    request: Mapped[Request] = relationship(back_populates='queries')
