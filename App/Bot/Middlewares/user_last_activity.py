from aiogram import BaseMiddleware

from App.Core.Database.Requests.middleware_rq import UpdateUserLastActivity


class UserLastActivityMiddleware(BaseMiddleware):
    def __init__(self, user_last_activity: UpdateUserLastActivity):
        self.user_last_activity = user_last_activity

    async def __call__(self, handler, event, data):
        telegram_user = data.get('event_from_user')

        if telegram_user:
            try:
                await self.user_last_activity.update_last_active(telegram_user.id)
            except:
                pass

        return await handler(event, data)
