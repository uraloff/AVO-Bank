from aiogram import Router, html
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command

from App.Core.Database.Requests import user_rq
from App.Bot.Keyboards import kb_keyboards as kb
from App.Bot.States.sending_phone_number import SendingPhoneNumber
from App.Bot.Keyboards.ikb_keyboards import lang_ikb, inline_builder


user_router = Router()


@user_router.message(CommandStart())
async def handle_start(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    username = message.from_user.username
    args = message.text.split(' ')
    user = await user_rq.get_user(user_id)

    await state.clear()

    # --- СЦЕНАРИЙ 1: НОВЫЙ ПОЛЬЗОВАТЕЛЬ ---
    if not user:
        referral_code = args[1] if len(args) > 1 else None
        
        await user_rq.set_user(
            telegram_id=user_id,
            full_name=user_full_name,
            username=username,
            referral_code=referral_code
        )
        await send_language_selection(message, user_full_name)
        
        return

    # --- СЦЕНАРИЙ 2: ПОЛЬЗОВАТЕЛЬ ЕСТЬ, НО НЕТ ЯЗЫКА ---
    if not user.language:
        await send_language_selection(message, user_full_name)

        return

    # --- СЦЕНАРИЙ 3: ЕСТЬ ЯЗЫК, НО НЕТ ТЕЛЕФОНА ---
    if not user.phone_number:
        if user.language == 'ru':
            await message.answer(
                "Пожалуйста, отправьте номер телефона, нажав на кнопку ниже 👇",
                reply_markup=kb.send_phone_kb
            )
        else:
            await message.answer(
                "Qaytganingiz bilan! Ro'yxatdan o'tishni yakunlash uchun telefon raqamingizni yuboring 👇",
                reply_markup=kb.send_phone_kb_uz
            )
        
        await state.set_state(SendingPhoneNumber.sending_phone_number)
        
        return

    # --- СЦЕНАРИЙ 4: ПОЛНОЦЕННЫЙ ПОЛЬЗОВАТЕЛЬ ---
    if user.language == 'ru':
        await message.answer("🏠 Главное меню", reply_markup=kb.main_kb)
        
        sent_message = await message.answer(
            "Добро пожаловать на домашнюю страницу! Вы можете узнать необходимую информацию, выбрав один из следующих вариантов",
            reply_markup=inline_builder(
                ['💸 Бонусы', '💳 AVO platinum', '🏦 О нас', '🔄 Операции', '🌟 Розыгрыш «AVO айфон марафон» 🌟'],
                ['ru_bonuses', 'ru_card', 'ru_about_us', 'ru_operations', 'ru_giveaway'],
                [2, 2, 1]
            )
        )
        
        await state.update_data(last_interface_msg_id=sent_message.message_id)
    else:
        sent_message = await message.answer(
            "Bosh sahifaga xush kelibsiz! Quyidagi variantlardan birini tanlab kerakli ma'lumotlarni olishingiz mumkin",
            reply_markup=inline_builder(
                # Твои кнопки на узбекском
                ['💸 Bonuslar', '💳 AVO platinum', '🏦 Biz haqimizda', '🔄 Amallar', '🌟 AVO iPhone marafoni 🌟'],
                ['uz_bonuses', 'uz_card', 'uz_about_us', 'uz_operations', 'uz_giveaway'],
                [2, 2, 1]
            )
        )
        await state.update_data(last_interface_msg_id=sent_message.message_id)


async def send_language_selection(message: Message, full_name: str):
    if message.from_user.language_code == 'ru':
        await message.answer(
            f"Привет, {html.bold(html.quote(full_name))}!\n"
            "Выберите язык 👇",
            reply_markup=lang_ikb
        )
    else:
        await message.answer(
            f"Salom, {html.bold(html.quote(full_name))}!\n"
            "Tilni tanlang 👇",
            reply_markup=lang_ikb
        )


@user_router.message(Command('change_language'))
async def change_language(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user = await user_rq.get_user(user_id)
    
    await state.clear()
    
    if not user.phone_number:
        await message.answer(
            "Пожалуйста, отправьте номер телефона, нажав на кнопку ниже 👇",
            reply_markup=kb.send_phone_kb
        )
        await state.set_state(SendingPhoneNumber.sending_phone_number)
        
        return

    if message.from_user.language_code == 'ru':
        await message.answer(
            f"Привет, {html.bold(html.quote(user_full_name))}!\n"
            "Выберите язык 👇",
            reply_markup=inline_builder(
                ["🇺🇿 O'zbek tili", "🇷🇺 Русский"],
                ["uz_after_change_lang", "ru_after_change_lang"]
            )
        )
    else:
        await message.answer(
            f"Salom, {html.bold(html.quote(user_full_name))}!\n"
            "Tilni tanlang 👇",
            reply_markup=inline_builder(
                ["🇺🇿 O'zbek tili", "🇷🇺 Русский"],
                ["uz_after_change_lang", "ru_after_change_lang"]
            )
        )