import datetime as dt

from sqlalchemy.orm import Mapped, mapped_column

from framework.db import Model


class Request(Model):
    """Request Model."""

    __tablename__ = 'requests'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[dt.datetime]
    duration: Mapped[float]
    url: Mapped[str]
