from sqlalchemy import update
from datetime import datetime

from App.Core.Database.Models.user import User


# ------------------------------ Обновление времени последней активности пользователя ------------------------------
class UpdateUserLastActivity:
    def __init__(self, session_pool):
        self.session_pool = session_pool

    async def update_last_active(self, telegram_id: int):
        """
        Обновляет время последнего активного действия пользователя.

        :param telegram_id: ID пользователя в Telegram
        :return: None
        """
        telegram_id = int(telegram_id)
        async with self.session_pool() as session:
            stmt = (
                update(User)
                .where(User.telegram_id == telegram_id)
                .values(last_active=datetime.now())
            )
            await session.execute(stmt)
            await session.commit()