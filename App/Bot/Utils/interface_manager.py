from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove

async def send_interface_message(
    bot: Bot,
    user_id: int,
    text: str,
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove,
    state: FSMContext = None, # Если есть текущий стейт
    fsm_storage = None # Если нужно получить чужой стейт
):
    """
    Отправляет сообщение и удаляет кнопки у предыдущего интерфейсного сообщения.
    Работает даже если мы отправляем сообщение другому юзеру (не тому, кто вызвал хендлер).
    """
    
    # 1. Если нам не передали state (или мы пишем другому юзеру), добываем контекст вручную
    target_state = state
    
    if not target_state and fsm_storage:
        # Создаем ключ для хранилища (user_id = chat_id в личке)
        key = StorageKey(bot_id=bot.id, chat_id=user_id, user_id=user_id)
        # Получаем контекст
        target_state = FSMContext(storage=fsm_storage, key=key)

    if target_state:
        # 2. Чистим старое
        data = await target_state.get_data()
        last_msg_id = data.get("last_interface_msg_id")
        
        if last_msg_id:
            try:
                await bot.edit_message_reply_markup(
                    chat_id=user_id,
                    message_id=last_msg_id,
                    reply_markup=None
                )
            except TelegramBadRequest:
                pass # Сообщение удалено или кнопок уже нет
    
    # 3. Отправляем новое
    sent_message = await bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=reply_markup
    )
    
    # 4. Сохраняем новое (ТОЛЬКО если есть доступ к стейту)
    if target_state:
        await target_state.update_data(last_interface_msg_id=sent_message.message_id)
        
    return sent_message