from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from App.keyboards import inline_builder
from Photo import img_handler as img


ru_user_router = Router()


# ----------------------------------------------КНОПКА "Русский язык"----------------------------------------------
@ru_user_router.callback_query(F.data.in_({'ru', 'ru_back_to_main_from_bonuses', 'ru_back_to_main_from_card', 'ru_back_to_main_from_operations', 'ru_back_to_main_from_about_us'}))
async def ru_user(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("Добро пожаловать на домашнюю страницу! Вы можете узнать необходимую информацию, выбрав один из следующих вариантов", 
                                     reply_markup=inline_builder(
                                        ['💸 Бонусы', '💳 AVO platinum', '🏦 О нас', '🔄 Операции', 'Назад ↩️'],
                                        ['ru_bonuses', 'ru_card', 'ru_about_us', 'ru_operations', 'ru_back_to_lang'],
                                        [2, 2, 1]
                                    )
        )
        await callback.answer("Выбран русский язык")
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("Добро пожаловать на домашнюю страницу! Вы можете узнать необходимую информацию, выбрав один из следующих вариантов",
                                     reply_markup=inline_builder(
                                        ['💸 Бонусы', '💳 AVO platinum', '🏦 О нас', '🔄 Операции', 'Назад ↩️'],
                                        ['ru_bonuses', 'ru_card', 'ru_about_us', 'ru_operations', 'ru_back_to_lang'],
                                        [2, 2, 1]
                                    )
    )
        await callback.answer("Выбран русский язык")



# -------------------------------------------------КНОПКА "Бонусы"-------------------------------------------------
@ru_user_router.callback_query(F.data == 'ru_bonuses')
async def ru_bonuses(callback: CallbackQuery) -> None:
    await callback.message.delete()    
    await callback.message.answer_photo(photo=img.about_bonus_ru_photo,
                                        caption="<b>Начисление бонусов:</b>\n• За <b>скачивание приложения</b> и <b>оформление</b> карты AVO platinum - 250 000 бонусов\n• Акция <b>«Приведи друга»</b> - за каждого друга — 50 000 бонусов, другу — 250 000 бонусов\n• В честь <b>дня рождения</b> - 100 000 бонусов\n• Максимальная сумма <b>бонусов в месяц</b> - 5 000 000 бонусов\n<b>Использование бонусов:</b>\n• Используйте бонусы, чтобы вернуть деньги <b>за платежи</b> и <b>комиссии за услуги Банка</b> - 1 бонус = 1 сум\n• Обмен бонусов для оплаты <b>комиссии Банка</b> - <b>до 100%за снятие наличных и переводы, обслуживание карты AVO platinum</b>\n• Обмен бонусов для оплаты <b>других услуг</b> - до 50 000 бонусов в месяц\n• <b>Срок действия</b> начисленных бонусов - 12 месяцев",
                                        reply_markup=inline_builder(
                                            ['Назад ↩️'],
                                            ['ru_back_to_main_from_bonuses']
                                        )
    )
    await callback.answer()


# ----------------------------------------------КНОПКА "AVO platinum"----------------------------------------------
@ru_user_router.callback_query(F.data.in_({'ru_card', 'ru_back_to_card_from_grace'}))
async def ru_card(callback: CallbackQuery) -> None:
    await callback.message.delete()    
    await callback.message.answer_photo(photo=img.about_card_ru_photo,
                                        caption="✅ <b>До 50 000 000 сумов</b>\nКредитный лимит на любые покупки\n\n✅ <b>0% до 45 дней</b>\nНа покупки по карте\n\n✅ <b>100% онлайн</b>\nБез залога и поручителей\n\n✅ <b>Бесплатный выпуск</b>\nВиртуальной карты AVO platinum\n\n✅ <b>Безопасная</b>\nЗащищена технологией 3D Secure\n\n✅ <b>По всему миру</b>\nЛюбые финансовые операции в любой точке мира",
                                        reply_markup=inline_builder(
                                            ['⭐ Льготный период', 'Назад ↩️'],
                                            ['ru_grace_period', 'ru_back_to_main_from_card']
                                        )
    )
    await callback.answer()


# ----------------КНОПКА "Льготный период" В "AVO platinum" И "30 дней" В "+15 дней"/"Время оплаты"-----------------
@ru_user_router.callback_query(F.data.in_({'ru_grace_period', 'ru_thirty'}))
async def ru_thirty(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>30 дней на покупки</b>\n\nВ течение 30 дней вы тратите деньги с кредитной карты, а в конце каждого льготного периода банк подсчитывает, сколько денег вы потратили, и присылает выписку",
                                         reply_markup=inline_builder(
                                             ['📅 +15 дней', "📌 Время оплаты", 'Назад ↩️'],
                                             ['ru_fifteen', 'ru_payment_time', 'ru_back_to_card_from_grace'],
                                             [2, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>30 дней на покупки</b>\n\nВ течение 30 дней вы тратите деньги с кредитной карты, а в конце каждого льготного периода банк подсчитывает, сколько денег вы потратили, и присылает выписку",
                                      reply_markup=inline_builder(
                                          ['📅 +15 дней', "📌 Время оплаты", 'Назад ↩️'],
                                          ['ru_fifteen', 'ru_payment_time', 'ru_back_to_card_from_grace'],
                                          [2, 1]
                                     )
        )
        await callback.answer()


# ----------------------------------КНОПКА "+15 дней" В "30 дней" И "Время оплаты"----------------------------------
@ru_user_router.callback_query(F.data == 'ru_fifteen')
async def ru_fifteen(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>Ещё 15 дней на оплату</b>\n\nДалее у вас остаётся еще 15 дней на оплату задолженности\n\nНапример, дата вашей выписки 5 августа, 14 августа была совершена первая покупка, а 25 августа — вторая\n\nДата формирования вашей выписки c расходами 5 сентября и если вы вернете всю потраченную сумму до 20 сентября (5 августа + 45 дней), проценты не начисляются и не придётся переплачивать\n\nПока идёт время на оплату долга по выписке, вы можете продолжать пользоваться картой\n\nРасходы за покупки, совершённые на следующий день выписки, пойдут уже в новый льготный период при условии, что в течение 15 дней будет внесён полный платеж за первый льготный период\n\nТаким образом, в день вашей выписки заканчивается один период льготных трат, а на следующий день уже начинается другой — для новых покупок",
                                         reply_markup=inline_builder(
                                             ['📅 30 дней', "📌 Время оплаты", 'Назад ↩️'],
                                             ['ru_thirty', 'ru_payment_time', 'ru_back_to_card_from_grace'],
                                             [2, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>Ещё 15 дней на оплату</b>\n\nДалее у вас остаётся еще 15 дней на оплату задолженности\n\nНапример, дата вашей выписки 5 августа, 14 августа была совершена первая покупка, а 25 августа — вторая\n\nДата формирования вашей выписки c расходами 5 сентября и если вы вернете всю потраченную сумму до 20 сентября (5 августа + 45 дней), проценты не начисляются и не придётся переплачивать\n\nПока идёт время на оплату долга по выписке, вы можете продолжать пользоваться картой\n\nРасходы за покупки, совершённые на следующий день выписки, пойдут уже в новый льготный период при условии, что в течение 15 дней будет внесён полный платеж за первый льготный период\n\nТаким образом, в день вашей выписки заканчивается один период льготных трат, а на следующий день уже начинается другой — для новых покупок",
                                      reply_markup=inline_builder(
                                          ['📅 30 дней', "📌 Время оплаты", 'Назад ↩️'],
                                          ['ru_thirty', 'ru_payment_time', 'ru_back_to_card_from_grace'],
                                          [2, 1]
                                     )
        )
        await callback.answer()


# ----------------------------------КНОПКА "Время оплаты" В "30 дней" И "+15 дней"----------------------------------
@ru_user_router.callback_query(F.data == 'ru_payment_time')
async def ru_payment_time(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>Покупаете раньше — больше времени на оплату</b>\n\nПродолжительность льготного периода по каждой конкретной покупке зависит от того, в какой день льготного периода вы её совершили\n\nК примеру, вы пользуетесь кредиткой AVO platinum с льготным периодом до 45 дней. Дата вашей выписки — 5-е число каждого месяца\n\nЕсли вы совершите покупку 6 августа — на следующий день после выписки — на эту покупку у вас будет максимальный льготный период трат 30 дней, а потом ещё 15 дней на возврат потраченных денег",
                                         reply_markup=inline_builder(
                                             ['📅 +15 дней', "📅 30 дней", 'Назад ↩️'],
                                             ['ru_fifteen', 'ru_thirty', 'ru_back_to_card_from_grace'],
                                             [2, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>Покупаете раньше — больше времени на оплату</b>\n\nПродолжительность льготного периода по каждой конкретной покупке зависит от того, в какой день льготного периода вы её совершили\n\nК примеру, вы пользуетесь кредиткой AVO platinum с льготным периодом до 45 дней. Дата вашей выписки — 5-е число каждого месяца\n\nЕсли вы совершите покупку 6 августа — на следующий день после выписки — на эту покупку у вас будет максимальный льготный период трат 30 дней, а потом ещё 15 дней на возврат потраченных денег",
                                      reply_markup=inline_builder(
                                          ['📅 +15 дней', "📅 30 дней", 'Назад ↩️'],
                                          ['ru_fifteen', 'ru_thirty', 'ru_back_to_card_from_grace'],
                                          [2, 1]
                                     )
        )
        await callback.answer()


# --------------------------------------------------КНОПКА "О нас"--------------------------------------------------
@ru_user_router.callback_query(F.data.in_({'ru_about_us', 'ru_back_to_about_us_from_documents'}))
async def ru_about_us(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer_photo(photo=img.about_us_ru_photo,
                                        caption="<b>Ценности</b>\n\nНаша система ценностей формирует нашу идентичность и определяет, как мы действуем\n✅ <b>Честно</b>\n       Выполняем обещания\n✅ <b>Любопытно</b>\n       Постоянно ищем новые решения, слышим обратную связь от каждого\n✅ <b>Просто</b>\n       Делаем просто и понятно для всех\n\n<b>Наша цель – улучшить жизнь клиентов</b>\nМы стремимся, чтобы наши клиенты могли чувствовать себя свободными, уверенными и современными, а также ощущать надёжность в завтрашнем дне\n\nДля достижения этой цели мы предоставляем высококачественные продукты и услуги, которые помогают нашим клиентам улучшить свою жизнь\n\n<b>AVO – сокращение от слова «havo», что означает «воздух»</b>\nКак воздух – невесомый, вездесущий, чистый, так и предоставляемые нами финансовые услуги доступны, понятны и легки в повседневном использовании",
                                        reply_markup=inline_builder(
                                            ['📃 Документы', 'Назад ↩️'],
                                            ['ru_documents', 'ru_back_to_main_from_about_us']
                                        )
    )
    await callback.answer()


# ------------------------------------------КНОПКА "Документы" В "О нас"--------------------------------------------
@ru_user_router.callback_query(F.data.in_({'ru_documents', 'ru_back_to_documents_from_for_clients', 'ru_back_to_documents_from_main_documents', 'ru_back_to_documents_from_important_facts', 'ru_back_to_documents_from_internal_regulatory_documents', 'ru_back_to_documents_from_affylated_persons', 'ru_back_to_documents_from_application_form', 'ru_back_to_documents_from_financial_statements', 'ru_back_to_documents_from_audit_reports', 'ru_back_to_documents_from_dividends'}))
async def ru_documents(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>Документы и лицензии</b>\n\nВы можете просмотреть документы, выбрав один из следующих вариантов 👇",
                                         reply_markup=inline_builder(
                                             ['📒 Клиентам', '📒 Основные документы', '📒 Существенные факты', '📒 Внутренние нормативные документы', '📒 Аффилированные лица', '📒 Формы заявлений', '📒 Финансовые отчёты', '📒 Аудиторские заключения', '📒 Дивиденды', 'Назад ↩️'],
                                             ['ru_for_clients', 'ru_main_documents', 'ru_important_facts_1', 'ru_internal_regulatory_documents_1', 'ru_affylated_persons', 'ru_application_form', 'ru_financial_statements', 'ru_audit_reports', 'ru_dividends', 'ru_back_to_about_us_from_documents'],
                                             [2, 2, 2, 2, 1, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>Документы и лицензии</b>\n\nВы можете просмотреть документы, выбрав один из следующих вариантов 👇",
                                      reply_markup=inline_builder(
                                          ['📒 Клиентам', '📒 Основные документы', '📒 Существенные факты', '📒 Внутренние нормативные документы', '📒 Аффилированные лица', '📒 Формы заявлений', '📒 Финансовые отчёты', '📒 Аудиторские заключения', '📒 Дивиденды', 'Назад ↩️'],
                                          ['ru_for_clients', 'ru_main_documents', 'ru_important_facts_1', 'ru_internal_regulatory_documents_1', 'ru_affylated_persons', 'ru_application_form', 'ru_financial_statements', 'ru_audit_reports', 'ru_dividends', 'ru_back_to_about_us_from_documents'],
                                          [2, 2, 2, 2, 1, 1]
                                     )
        )
        await callback.answer()


# -----------------------------------------КНОПКА "Клиентам" В "Документы"-----------------------------------------
@ru_user_router.callback_query(F.data == 'ru_for_clients')
async def ru_for_clients(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Клиентам</b>\n\n📄 <a href='https://docs.avo.uz/AVO_dkbo_ru.pdf'>Условия комплексного банковского обслуживания (действует с 29.04.2024)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_loyalty_ru.pdf'>Общие условия программы лояльности АО «AVO bank» (действует с 29.03.2024)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_referral_ru.pdf'>Правила проведения Акции «Приведи друга на кредитную карту» (действует с 29.03.2024)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_user_agreement_ru.pdf'>Пользовательское соглашение</a>\n\n📄 <a href='https://docs.avo.uz/AVO_privacy_policy_web_ru.pdf'>Политика конфиденциальности</a>\n\n📄 <a href='https://docs.avo.uz/AVO_tariffs_ru.pdf'>Тарифы</a>\n\n📄 <a href='https://docs.avo.uz/AVO_bank_partners_ru.pdf'>Партнёры Банка</a>\n\n📄 <a href='https://docs.avo.uz/AVO_consent_form_ru.pdf'>Форма согласия на обработку персональных данных и получение кредитного отчета из кредитного бюро</a>\n\n📄 <a href='https://docs.avo.uz/AVO_rules_for_using_ATMs_ru.pdf'>Правила пользования банкоматами AVO</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_for_clients']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# -------------------------------------КНОПКА "Основные документы" В "Документы"-------------------------------------
@ru_user_router.callback_query(F.data == 'ru_main_documents')
async def ru_main_documents(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Основные документы</b>\n\n📄 <a href='https://docs.avo.uz/AVO_Article_of_Association_ru.pdf'>Устав</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Banking_License_ru.pdf'>Лицензия</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Amendments_to_the_Articles_of_Association_ru.pdf'>Изменения к Уставу №1</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Amendments_to_the_Articles_of_Association_240329_ru.pdf'>Изменения к Уставу №2</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_main_documents']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------КНОПКА "Существенные факты" В "Документы" И "Страница 1" В "Страница 2"----------------------
@ru_user_router.callback_query(F.data == 'ru_important_facts_1')
async def ru_important_facts_1(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Существенные факты</b>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.06_6.pdf'>Существенный факт №6 от 06.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.16_21.pdf'>Существенный факт №21 от 16.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.16_6.pdf'>Существенный факт №6 от 16.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.19_8.pdf'>Существенный факт №8 от 19.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.19_21_2.pdf'>Существенный факт №21 от 19.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.22_36.pdf'>Существенный факт №36 от 22.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.22_21.pdf'>Существенный факт №21 от 22.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.02.02_6.pdf'>Существенный факт №6 от 02.02.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.02.02_8.pdf'>Существенный факт №8 от 02.02.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material%20fact_24.02.28_6.pdf'>Существенный факт №6 от 28.02.2024</a>",
                                     reply_markup=inline_builder(
                                         ['Страница 2 ➡️', 'Назад ↩️'],
                                         ['ru_important_facts_2', 'ru_back_to_documents_from_important_facts']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ----------------------------------------КНОПКА "Страница 2" В "Страница 1"----------------------------------------
@ru_user_router.callback_query(F.data == 'ru_important_facts_2')
async def ru_important_facts_2(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Существенные факты</b>\n\n📄 <a href='https://docs.avo.uz/AVO_material%20fact_24.02.28_36.pdf'>Существенный факт №36 от 28.02.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material%20fact_24.03.20_6.pdf'>Существенный факт №6 от 20.03.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.04.25_21.pdf'>Существенный факт №21 от 25.04.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.05.14_6.pdf'>Существенный факт №6 от 14.05.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.05.22_6.pdf'>Существенный факт №6 от 22.05.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.05.22_2.pdf'>Существенный факт №2 от 22.05.2024</a>",
                                     reply_markup=inline_builder(
                                         ['Страница 1 ⬅️', 'Назад ↩️'],
                                         ['ru_important_facts_1', 'ru_back_to_documents_from_important_facts']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# --------------КНОПКА "Внутренние нормативные документы" В "Документы" И "Страница 1" В "Страница 2"--------------
@ru_user_router.callback_query(F.data == 'ru_internal_regulatory_documents_1')
async def ru_internal_regulatory_documents_1(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Внутренние нормативные документы</b>\n\n📄 <a href='https://docs.avo.uz/AVO_corporate_governance_policy_ru.pdf'>Политика по корпоративному управлению</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Regulations_Sole_Shareholder_ru.pdf'>Положение о высшем органе управления (Единственном акционере)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_supervisory_board_ru.pdf'>Положение о Наблюдательном совете</a>\n\n📄 <a href='https://docs.avo.uz/AVO_executive_board_ru.pdf'>Положение об исполнительном органе (правлении)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_internal_audit_service_ru.pdf'>Положение о Службе внутреннего аудита</a>\n\n📄 <a href='https://docs.avo.uz/AVO_conflict_of_interest_policy_ru.pdf'>Политика по предотвращению и урегулированию конфликта интересов</a>\n\n📄 <a href='https://docs.avo.uz/AVO_disclosure_policy_ru.pdf'>Политика по раскрытию сведений</a>\n\n📄 <a href='https://docs.avo.uz/AVO_dividend_policy_ru.pdf'>Политика по выплате дивидендов</a>\n\n📄 <a href='https://docs.avo.uz/AVO_business_plan_and_development_strategy_ru.pdf'>Бизнес-план и стратегия развития</a>\n\n📄 <a href='https://docs.avo.uz/AVO_bank_regulations_ru.pdf'>Положение о порядке рассмотрения обращений физических и юридических лиц</a>",
                                     reply_markup=inline_builder(
                                         ['Страница 2 ➡️', 'Назад ↩️'],
                                         ['ru_internal_regulatory_documents_2', 'ru_back_to_documents_from_internal_regulatory_documents']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ----------------------------------------КНОПКА "Страница 2" В "Страница 1"----------------------------------------
@ru_user_router.callback_query(F.data == 'ru_internal_regulatory_documents_2')
async def ru_internal_regulatory_documents_2(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Внутренние нормативные документы</b>\n\n📄 <a href='https://docs.avo.uz/AVO_Corporate_Ethics_Code_ru.pdf'>Кодекс корпоративной этики</a>",
                                     reply_markup=inline_builder(
                                         ['Страница 1 ⬅️', 'Назад ↩️'],
                                         ['ru_internal_regulatory_documents_1', 'ru_back_to_documents_from_internal_regulatory_documents']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ------------------------------------КНОПКА "Аффилированные лица" В "Документы"------------------------------------
@ru_user_router.callback_query(F.data == 'ru_affylated_persons')
async def ru_affylated_persons(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Аффилированные лица</b>\n\n📄 <a href='https://docs.avo.uz/AVO_affiliates.pdf'>Список аффилированных лиц</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_affylated_persons']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# --------------------------------------КНОПКА "Формы заявлений" В "Документы"--------------------------------------
@ru_user_router.callback_query(F.data == 'ru_application_form')
async def ru_application_form(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Формы заявлений</b>\n\n📄 <a href='https://docs.avo.uz/Antifraud_form_ru.pdf'>Форма для принятия обращения клиента по антифроду</a>\n\n📄 <a href='https://avo.uz/ru/contract-termination'>Инструкция по расторжению договора</a>\n\n📄 <a href='https://docs.avo.uz/application_for_disput_ru.pdf'>Заявление на разрешение спорной транзакции</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_application_form']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# -------------------------------------КНОПКА "Финансовые отчёты" В "Документы"-------------------------------------
@ru_user_router.callback_query(F.data == 'ru_financial_statements')
async def ru_financial_statements(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Финансовые отчёты</b>\n\n📄 <a href='https://docs.avo.uz/AVO_financial_statements.pdf'>Годовой отчёт по итогам 2023 года</a>\n\n📄 <a href='https://docs.avo.uz/AVO_first_quartile.pdf'>Отчёт за 1 квартал 2024 года</a>\n\n📄 <a href='https://docs.avo.uz/AVO_first_quartile_emitter.pdf'>Отчёт эмитента по итогам 1 квартала 2024 года</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_financial_statements']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# -----------------------------------КНОПКА "Аудиторские заключения" В "Документы"-----------------------------------
@ru_user_router.callback_query(F.data == 'ru_audit_reports')
async def ru_audit_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Аудиторские заключения</b>\n\n📄 <a href='https://docs.avo.uz/AVO_financial_statements.pdf'>Годовой отчёт по итогам 2023 года</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_audit_reports']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# -----------------------------------------КНОПКА "Дивиденды" В "Документы"-----------------------------------------
@ru_user_router.callback_query(F.data == 'ru_dividends')
async def ru_dividends(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Дивиденды</b>\n\n📄 <a href='https://docs.avo.uz/AVO_dividend_payment_ru.pdf'>Распределенные и выплаченные дивиденды за последние 3 года</a>",
                                     reply_markup=inline_builder(
                                         ['Назад ↩️'],
                                         ['ru_back_to_documents_from_dividends']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# -------------------------------------------------КНОПКА "Операции"-------------------------------------------------
@ru_user_router.callback_query(F.data.in_({'ru_operations', 'ru_back_to_operations_from_other_tariffs'}))
async def ru_operations(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Переводы и снятие наличных</b>\n\n• Снятие наличных или переводы c карты на карту <b>из собственных</b> средств:\n- бесплатно, в банкоматах и мобильном приложении AVO\n- 0,5% от суммы операции в сторонних\n• Снятие наличных или переводы c карты на карту <b>из кредитных средств</b>:\n- 29 000 сумов + 2,9% от суммы операции\n• Лимит на снятие наличных и переводы:\n- <b>по карте AVO platinum</b> — 5 000 000 сумов за операцию, 50 000 000 сумов в месяц\n- <b>по сторонним картам</b> — 5 000 000 сумов за операцию, 50 000 000 сумов в месяц\n• Платежи с использованием <b>собственных средств</b>:\n- бесплатно, в мобильном приложении AVO\n• Платежи с использованием <b>кредитных средств</b>:\n- бесплатно <i>(за исключением операций, отнесенных к нельготным операциям)</i>, в мобильном приложении AVO",
                                     reply_markup=inline_builder(
                                         ['📑 Другие тарифы', 'Назад ↩️'],
                                         ['ru_other_tariffs_1', 'ru_back_to_main_from_operations']
                                    )
    )
    await callback.answer()


# ------------------------КНОПКА "Другие тарифы" В "Операции" И "Страница 1" В "Страница 2"------------------------
@ru_user_router.callback_query(F.data == 'ru_other_tariffs_1')
async def ru_other_tariffs_1(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Услуги, связанные с AVO Bank</b>\n\n• Запрос баланса карты AVO platinum в банкоматах AVO\n- бесплатно <i>(в сторонних — 11 000 сумов)</i>\n• Запрос баланса карты AVO platinum в мобильном приложении, по телефону в Контакт-центре\n- бесплатно\n• Услуга 3D Secure\n- бесплатно\n• Внесение карты в международный стоп-лист\n- 150 000 сумов\n• SMS/PUSH уведомление\n- 11 900 сумов в месяц",
                                     reply_markup=inline_builder(
                                         ['Страница 2 ➡️', 'Назад ↩️'],
                                         ['ru_other_tariffs_2', 'ru_back_to_operations_from_other_tariffs']
                                    )
    )
    await callback.answer()


# ----------------------------------------КНОПКА "Страница 2" В "Страница 1"----------------------------------------
@ru_user_router.callback_query(F.data == 'ru_other_tariffs_2')
async def ru_other_tariffs_2(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Обслуживание карт сторонних банков</b>\n\n• Платежи в банкоматах и мобильном приложении AVO\n- бесплатно <i>(в случае взимания комиссии, размер комиссии будет уточнен в момент совершения операции)</i>\n• AVO bankomatlaridan naqd pul yechib olish\n- operatsiya summasidan 1%\n• Снятие наличных с карты в банкоматах AVO\n- 1% от суммы операции\n• Пополнение карты в банкоматах AVO\n- 0,5% от суммы операции\n• Комиссия за переводы в банкоматах и мобильном приложении AVO\n- до 3 000 000 сумов бесплатно, от 3 000 000 — 0,5% в случае, когда получателем НЕ является карта AVO platinum\n• Запрос баланса в банкоматах AVO\n- 11 000 сумов\n• Операции с конвертацией валют в банкоматах и мобильном приложении AVO\n- курс Банка + 3% от суммы операции",
                                     reply_markup=inline_builder(
                                         ['Страница 1 ⬅️', 'Назад ↩️'],
                                         ['ru_other_tariffs_1', 'ru_back_to_operations_from_other_tariffs']
                                    )
    )
    await callback.answer()
