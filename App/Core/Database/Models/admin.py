from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, BigInteger, ForeignKey

from App.Core.Database.Requests.session import Base


class Admin(Base):
    __tablename__ = 'admins'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.telegram_id', ondelete='CASCADE'), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=lambda: datetime.now().replace(microsecond=0))