from os import getenv

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from App.Core.Database.Requests import admin_rq, user_rq
from App.Bot.Keyboards.ikb_keyboards import inline_builder


admin_router = Router()


@admin_router.message(F.text == getenv('ADMIN_SECRET_CODE'))
async def admin_login(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    user_full_name = message.from_user.full_name
    user = await user_rq.get_user(user_id)
    admin = await admin_rq.get_admin(user_id)

    await state.clear()

    if admin:
        if admin.user.language == 'ru':
            sent_message = await message.answer(
                "✅ Вы уже являетесь администратором",
                reply_markup=inline_builder(
                    ["Главное меню 🏠"],
                    ['ru_main_menu']
                )
            )
        else:
            sent_message = await message.answer(
                "✅ Siz allaqachon administrator hisoblanasiz",
                reply_markup=inline_builder(
                    ["Asosiy menyu 🏠"],
                    ['uz_main_menu']
                )
            )
    else:
        if user.language == 'ru':
            sent_message = await message.answer(
                "⏳ Ваша заявка на получение прав администратора отправлена на рассмотрение",
                reply_markup=inline_builder(
                    ["Главное меню 🏠"],
                    ['ru_main_menu']
                )
            )
        else:
            sent_message = await message.answer(
                "⏳ Administratorlik huquqlarini olish bo'yicha arizangiz ko'rib chiqish uchun yuborildi",
                reply_markup=inline_builder(
                    ["Asosiy menyu 🏠"],
                    ['uz_main_menu']
                )
            )

    await state.update_data(last_interface_msg_id=sent_message.message_id)
    await message.bot.send_message(
        chat_id=getenv('SUPER_ADMIN_ID'),
        text=(
             "<b>👤 Новый запрос на администратора:</b>\n\n"
            f"<b>Имя:</b> {user_full_name}\n"
            f"<b>ID:</b> {user_id}\n"
            f"<b>Имя пользователя:</b> {'@' + username if username else '-'}\n"
            f"<b>Номер телефона:</b> +{user.phone_number}\n"
        ),
        reply_markup=inline_builder(
            text=["❌ Отклонить", "✅ Одобрить"],
            callback_data=[f'reject_admin:{user_id}', f'approve_admin:{user_id}'],
            sizes=2
        )
    )


@admin_router.callback_query(F.data.startswith(('reject_admin:', 'approve_admin:')))
async def confirming_admin(callback: CallbackQuery, state: FSMContext) -> None:
    username = callback.from_user.username
    user_full_name = callback.from_user.full_name
    user_id = int(callback.data.split(':')[1])
    user = await user_rq.get_user(user_id)
    
    await state.clear()

    if callback.data.startswith('reject_admin:'):
        await callback.message.edit_text(
             "❌ Запрос на получение прав администратора отклонен\n\n"
            f"<b>Имя:</b> {user_full_name}\n"
            f"<b>ID:</b> {user_id}\n"
            f"<b>Имя пользователя:</b> {'@' + username if username else '-'}\n"
            f"<b>Номер телефона:</b> +{user.phone_number}\n"
        )
        
        if user.language == 'ru':
            sent_message = await callback.message.bot.send_message(
                chat_id=user_id,
                text="❌ Ваш запрос на получение прав администратора был отклонен.",
                reply_markup=inline_builder(
                    ["Главное меню 🏠"],
                    ['ru_main_menu']
                )
            )
        else:
            sent_message = await callback.message.bot.send_message(
                chat_id=user_id,
                text="❌ Administratorlik huquqlarini olish bo'yicha arizangiz rad etildi",
                reply_markup=inline_builder(
                    ["Asosiy menyu 🏠"],
                    ['uz_main_menu']
                )
            )

        await state.update_data(last_interface_msg_id=sent_message.message_id)
    else:
        await admin_rq.set_admin(user_id)
        await callback.message.edit_text(
             "✅ Запрос на получение прав администратора одобрен\n\n"
            f"<b>Имя:</b> {user_full_name}\n"
            f"<b>ID:</b> {user_id}\n"
            f"<b>Имя пользователя:</b> {'@' + username if username else '-'}\n"
            f"<b>Номер телефона:</b> +{user.phone_number}\n"
        )
        
        if user.language == 'ru':
            sent_message = await callback.message.bot.send_message(
                chat_id=user_id,
                text="🎉 Поздравляем! Ваш запрос на получение прав администратора был одобрен",
                reply_markup=inline_builder(
                    ["Главное меню 🏠"],
                    ['ru_main_menu']
                )
            )
        else:
            sent_message = await callback.message.bot.send_message(
                chat_id=user_id,
                text="🎉 Tabriklaymiz! Sizning administratorlik huquqlarini olish bo'yicha arizangiz ma'qullandi",
                reply_markup=inline_builder(
                    ["Asosiy menyu 🏠"],
                    ['uz_main_menu']
                )
            )

        await state.update_data(last_interface_msg_id=sent_message.message_id)