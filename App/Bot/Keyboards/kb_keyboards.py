from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


send_phone_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📱 Отправить номер телефона", request_contact=True)]
],
    resize_keyboard=True,
    one_time_keyboard=True
)


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📝 Задать вопрос")]
],
    resize_keyboard=True,
    one_time_keyboard=True
)


connect_operator_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📞 Связаться с оператором")]
],
    resize_keyboard=True,
    one_time_keyboard=True
)


def reply_builder(
        text: str | list[str],
        sizes: int | list[int] = 2,
        resize_keyboard: bool = True,
        one_time_keyboard: bool = True,
        **kwargs
) -> ReplyKeyboardMarkup:
    
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    for txt in text:
        builder.button(text=txt)

    builder.adjust(*sizes) if isinstance(sizes, list) else builder.adjust(sizes)

    return builder.as_markup(
        resize_keyboard=resize_keyboard,
        one_time_keyboard=one_time_keyboard,
        **kwargs
    )