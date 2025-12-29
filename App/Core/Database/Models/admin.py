from datetime import datetime

from sqlalchemy import DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from App.Core.Database.Models.user import User
from App.Core.Database.Requests.session import Base


class Admin(Base):
    __tablename__ = 'admins'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.telegram_id', ondelete='CASCADE'), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=lambda: datetime.now().replace(microsecond=0))
    user: Mapped["User"] = relationship(lazy="joined")