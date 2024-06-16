from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from App.keyboards import lang_ikb


user_router = Router()


@user_router.message(CommandStart())
@user_router.callback_query(F.data.in_({'uz_back_to_lang', 'ru_back_to_lang'}))
async def handle_start(message: Message | CallbackQuery) -> None:
    if message.from_user.language_code == "ru":
        if isinstance(message, CallbackQuery):
            await message.message.edit_text(f"Привет, {html.bold(html.quote(message.from_user.full_name))}!\nДля начала выберите язык 👇", 
                                            reply_markup=lang_ikb)
            await message.answer()
        else:
            await message.answer(f"Привет, {html.bold(html.quote(message.from_user.full_name))}!\nДля начала выберите язык 👇",
                                 reply_markup=lang_ikb)
    else:
        if isinstance(message, CallbackQuery):
            await message.message.edit_text(f"Salom, {html.bold(html.quote(message.from_user.full_name))}!\nAvval tilni tanlang 👇", 
                                            reply_markup=lang_ikb)
            await message.answer()
        else:
            await message.answer(f"Salom, {html.bold(html.quote(message.from_user.full_name))}!\nAvval tilni tanlang 👇",
                                 reply_markup=lang_ikb)
