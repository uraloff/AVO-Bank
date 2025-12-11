import enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, BigInteger, Enum

from App.Core.Database.Requests.session import Base

class UserStatus(enum.Enum):
    default = 'default'
    authenticated = 'authenticated'

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id = mapped_column(BigInteger, unique=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    joined_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=lambda: datetime.now().replace(microsecond=0))
    language: Mapped[str] = mapped_column(String(2), nullable=True)
    referral_code: Mapped[str] = mapped_column(String(50), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    last_active: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=lambda: datetime.now().replace(microsecond=0), onupdate=lambda: datetime.now().replace(microsecond=0))
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus, native_enum=False, length=50), default=UserStatus.default, server_default='default', nullable=False)