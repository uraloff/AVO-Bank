from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func, update, delete

from App.Core.Database.Models.user import User, UserStatus
from App.Core.Database.Requests.session import async_session


# ------------------------------ Создание нового пользователя ------------------------------
async def set_user(telegram_id: int, full_name: str, username: str | None = None, referral_code: str | None = None) -> None:
    """
    Создает нового пользователя в базе данных со стартовыми параметрами. Поля `joined_at` и `last_active` устанавливаются на текущее время.
    
    :param telegram_id: ID пользователя в Telegram
    :param full_name: Полное имя пользователя в Telegram
    :param username: Имя пользователя в Telegram (опционально)
    :param referral_code: Реферальный код пользователя (опционально). Необходим для отслеживания источника прихода новых пользователей
    :param status: Статус пользователя (по умолчанию default)
    :return: None
    """
    
    async with async_session() as session:
        user = User(
            telegram_id=telegram_id,
            full_name=full_name,
            username=username,
            referral_code=referral_code,
            status=UserStatus.default,
        )
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
        else:
            await session.refresh(user)


# ------------------------------ Получение пользователя ------------------------------
async def get_user(telegram_id: int) -> User | None:
    """
    Получает пользователя по его Telegram ID.

    :param telegram_id: ID пользователя в Telegram
    :return: Объект пользователя или None, если пользователь не найден
    """
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        return user


# ------------------------------ Обновление информации о пользователе ------------------------------
async def update_user(telegram_id: int, **kwargs) -> None:
    """
    Обновляет информацию о пользователе по его Telegram ID.

    :param telegram_id: ID пользователя в Telegram
    :param kwargs: Ключевые слова для обновления полей пользователя
    :return: None
    """
    async with async_session() as session:
        await session.execute(
            update(User)
            .where(User.telegram_id == telegram_id)
            .values(**kwargs)
        )
        await session.commit()


# ------------------------------ Установка языка пользователю ------------------------------
async def set_user_language(telegram_id: int, language: str) -> None:
    """
    Устанавливает язык пользователя по его Telegram ID.
    
    :param telegram_id: ID пользователя в Telegram
    :param language: Язык пользователя
    :return: None
    """
    async with async_session() as session:
        await session.execute(
            update(User)
            .where(User.telegram_id == telegram_id)
            .values(language=language)
        )
        await session.commit()
    

# ------------------------------ Установка номера телефона пользователю ------------------------------
async def set_user_phone_number(telegram_id: int, phone_number: str) -> None:
    """
    Устанавливает номер телефона пользователя по его Telegram ID.
    
    :param telegram_id: ID пользователя в Telegram
    :param phone_number: Номер телефона пользователя
    :return: None
    """
    async with async_session() as session:
        await session.execute(
            update(User)
            .where(User.telegram_id == telegram_id)
            .values(phone_number=phone_number)
        )
        await session.commit()