from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from framework.db import Model

if TYPE_CHECKING:
    from query_tracer.request.models.query import Query


class Request(Model):
    """Request Model."""

    __tablename__ = 'requests'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    timestamp: Mapped[dt.datetime]
    duration: Mapped[float]
    url: Mapped[str]
    queries: Mapped[list[Query]] = relationship(back_populates='request')
