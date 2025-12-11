from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lang_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="uz")],
    [InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="ru")]
])


def inline_builder(
        text: str | list[str],
        callback_data: str | list[str],
        sizes: int | list[int]=1,
        **kwargs
) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback_data, str):
        callback_data = [callback_data]
    if isinstance(sizes, int):
        sizes = [sizes]

    [
        builder.button(text=txt, callback_data=cb)
        for txt, cb in zip(text, callback_data)
    ]

    builder.adjust(*sizes)
    return builder.as_markup(**kwargs)
