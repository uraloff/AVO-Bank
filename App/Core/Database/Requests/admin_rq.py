from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func, update, delete

from App.Core.Database.Models.admin import Admin
from App.Core.Database.Requests.session import async_session


# ------------------------------ Создание нового админа ------------------------------
async def set_admin(telegram_id: int) -> None:
    """
    Создает нового админа в базе данных

    :param telegram_id: ID админа в Telegram
    :return: None
    """

    async with async_session() as session:
        admin = Admin(
            telegram_id=telegram_id
        )
        session.add(admin)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
        else:
            await session.refresh(admin)


# ------------------------------ Получение админа ------------------------------
async def get_admin(telegram_id: int) -> Admin | None:
    """
    Получает админа по его Telegram ID.

    :param telegram_id: ID админа в Telegram
    :return: Объект админа или None, если админ не найден
    """
    async with async_session() as session:
        result = await session.execute(
            select(Admin).where(Admin.telegram_id == telegram_id)
        )
        admin = result.scalar_one_or_none()
        return admin