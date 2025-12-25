from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Message
from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

class AutoClearInlineKeyboardMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:
        # Достаем состояние (FSM)
        state: FSMContext = data.get("state")
        
        if state:
            state_data = await state.get_data()
            last_msg_id = state_data.get("last_interface_msg_id")

            # Если есть сохраненный ID сообщения с кнопками
            if last_msg_id:
                try:
                    # Пытаемся убрать кнопки (reply_markup=None)
                    # Мы не удаляем само сообщение, а только кнопки, чтобы сохранить историю переписки
                    await event.bot.edit_message_reply_markup(
                        chat_id=event.chat.id,
                        message_id=last_msg_id,
                        reply_markup=None
                    )
                except TelegramBadRequest as e:
                    # Ошибка возникает, если:
                    # 1. Сообщение уже удалено
                    # 2. Кнопки уже удалены
                    # 3. Сообщение слишком старое (больше 48 часов)
                    print("⚠️ Не удалось очистить inline-клавиатуру:", e)
                
                # Важно: очищаем запись, чтобы не пытаться удалить снова
                await state.update_data(last_interface_msg_id=None)

        return await handler(event, data)