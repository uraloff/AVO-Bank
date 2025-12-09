import enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, BigInteger, ForeignKey, Enum

from App.Core.Database.Requests.session import Base


class OperatorStatus(enum.Enum):
    busy = 'busy'
    ready = 'ready'
    lunch = 'lunch'
    not_ready = 'not_ready'
    personal_time = 'personal_time'

class Operator(Base):
    __tablename__ = 'operators'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.telegram_id', ondelete='CASCADE'), unique=True, nullable=False)
    telegram_full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    real_full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=lambda: datetime.now().replace(microsecond=0))
    status: Mapped[OperatorStatus] = mapped_column(Enum(OperatorStatus, native_enum=False, length=50), default=OperatorStatus.ready, server_default='default', nullable=False)