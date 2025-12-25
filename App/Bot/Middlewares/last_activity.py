from aiogram import BaseMiddleware

from App.Core.Database.Requests.middleware_rq import UpdateLastActivity


class LastActivityMiddleware(BaseMiddleware):
    def __init__(self, last_activity: UpdateLastActivity):
        self.last_activity = last_activity

    async def __call__(self, handler, event, data):
        telegram_user = data.get('event_from_user')

        if telegram_user:
            try:
                await self.last_activity.update_last_active(telegram_user.id)
            except Exception as e:
                print("⚠️ Не удалось обновить время последней активности пользователя в БД.", e)

        return await handler(event, data)
