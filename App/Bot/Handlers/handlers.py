from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from App.Bot.Keyboards.keyboards import lang_ikb
from App.Core.Database.Requests import user_rq


user_router = Router()


@user_router.message(CommandStart())
@user_router.message(Command('change_language'))
async def handle_start(message: Message | CallbackQuery) -> None:
    args = message.text.split(' ')
    user_id = message.from_user.id
    username = message.from_user.username
    user_full_name = message.from_user.full_name
    user_language = await user_rq.get_user_language(user_id)
        
    if len(args) > 1:
        referral_code = args[1]

        await user_rq.set_user(
            telegram_id=user_id,
            full_name=user_full_name,
            username=username,
            referral_code=referral_code
        )
    else:
        await user_rq.set_user(
            telegram_id=user_id,
            full_name=user_full_name,
            username=username
        )

    if user_language == 'ru' or (message.from_user.language_code == 'ru' and user_language is None):
        await message.answer(
            f"Привет, {html.bold(html.quote(user_full_name))}!\n"
            "Выберите язык 👇",
            reply_markup=lang_ikb
        )
    else:
        await message.answer(
            f"Salom, {html.bold(html.quote(user_full_name))}!\n"
            "Tilni tanlang 👇",
            reply_markup=lang_ikb
        )