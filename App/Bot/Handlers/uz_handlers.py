from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from Photo import img_handler as img
from App.Bot.Keyboards.keyboards import inline_builder
from App.Core.Database.Requests import user_rq


uz_user_router = Router()


# ----------------------------------------------"O'zbek tili" KNOPKASI---------------------------------------------
@uz_user_router.callback_query(F.data.in_({'uz', 'uz_back_to_main_from_bonuses', 'uz_back_to_main_from_card', 'uz_back_to_main_from_operations', 'uz_back_to_main_from_about_us'}))
async def uz_user(callback: CallbackQuery) -> None:
    await user_rq.set_user_language(callback.from_user.id, 'uz')

    try:
        await callback.message.edit_text("Bosh sahifaga xush kelibsiz! Quyidagilardan birini tanlab o'zingizga kerakli bo'lgan ma'lumotlarni bilib olishingiz mumkin",
                                         reply_markup=inline_builder(
                                             ['💸 Bonuslar', '💳 AVO platinum', '🏦 Biz haqimizda', '🔄 Operatsiyalar', 'Ortga qaytish ↩️'],
                                             ['uz_bonuses', 'uz_card', 'uz_about_us', 'uz_operations', 'uz_back_to_lang'],
                                             [2, 2, 1]
                                         )
        )
        await callback.answer("O'zbek tili tanlandi")
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("Bosh sahifaga xush kelibsiz! Quyidagilardan birini tanlab o'zingizga kerakli bo'lgan ma'lumotlarni bilib olishingiz mumkin",
                                      reply_markup=inline_builder(
                                          ['💸 Bonuslar', '💳 AVO platinum', '🏦 Biz haqimizda', '🔄 Operatsiyalar', 'Ortga qaytish ↩️'],
                                          ['uz_bonuses', 'uz_card', 'uz_about_us', 'uz_operations', 'uz_back_to_lang'],
                                          [2, 2, 1]
                                      )
        )
        await callback.answer("O'zbek tili tanlandi")


# -----------------------------------------------"Bonuslar" KNOPKASI-----------------------------------------------
@uz_user_router.callback_query(F.data == 'uz_bonuses')
async def uz_bonuses(callback: CallbackQuery) -> None:
    await callback.message.delete()    
    await callback.message.answer_photo(photo=img.about_bonus_uz_photo,
                                        caption="<b>25 000 bonus pulni qanday olish mumkin?</b>\nAVO da ro'yxatdan o'ting va AVO platinum kartasini rasmiylashtiring, shunda <b>25 000 bonus so'm</b> olishingiz mumkin. AVO platinum kartasi bloklanganda, bonuslardan foydalanib bo'lmaydi. Bonuslarning amal qilish muddati - olingan sanadan boshlab <b>12 oy</b>. Ko'proq bonuslar olish uchun esa do'stlaringizni AVO ga taklif qiling - AVO ga taklif qilingan har bir do'st uchun <b>50 000 so'm</b>\n\n<b>Bonus pullarni nimaga sarflash mumkin?</b>\nSiz komissiyani quyidagi hollarda qaytarishingiz mumkin:\n• Karta xizmati\n• Naqd pul yechib olish\n• Pul o'tkazmalari\n\n<b>Foydali bo'lishi mumkin</b>\n• AVO to'lovlari cheklovlarsiz qaytariladi.\n• Kompensatsiya 30 kundan ortiq bo'lmagan muddatda amalga oshirilgan operatsiyalar uchun mavjud.\n• Siz oyiga 500 000 dan ortiq bo'lmagan bonuslarni olshingiz mumkin.",
                                        reply_markup=inline_builder(
                                            ['Ortga qaytish ↩️'],
                                            ['uz_back_to_main_from_bonuses']
                                        )
    )
    await callback.answer()


# ---------------------------------------------"AVO platinum" KNOPKASI---------------------------------------------
@uz_user_router.callback_query(F.data.in_({'uz_card', 'uz_back_to_card_from_grace'}))
async def uz_card(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer_photo(photo=img.about_card_uz_photo,
                                        caption="✅ <b>50 000 000 so'mgacha</b>\nIstalgan xarid uchun kredit limiti\n\n✅ <b>45 kungacha 0%</b>\nKarta bo'yicha xaridlar uchun\n\n✅ <b>100% onlayn</b>\nGarovsiz va kafillarsiz\n\n✅ <b>Kartani bepul chiqarish</b>\nAVO platinum kartasini bepul oching\n\n✅ <b>Xavfsiz</b>\n3D Secure texnologiyasi bilan himoyalangan\n\n✅ <b>Butun dunyo bo'ylab</b>\nMoliyaviy operatsiyalarni dunyoning istalgan nuqtasida amalga oshiring",
                                        reply_markup=inline_builder(
                                            ['⭐ Imtiyozli davr', 'Ortga qaytish ↩️'],
                                            ['uz_grace_period', 'uz_back_to_main_from_card']
                                        )
    )
    await callback.answer()


# -------------"AVO platinum" DAGI "Imtiyozli davr" VA "+15 kun"/"To'lov vaqti" DAGI "30 kun" KNOPKASI-------------
@uz_user_router.callback_query(F.data.in_({'uz_grace_period', 'uz_thirty'}))
async def uz_thirty(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>Xaridlaringiz uchun 30 kun</b>\n\nSiz kredit kartadan istalgan xaridlaringiz uchun 30 kun ichida pul sarflashingiz mumkin, har imtiyozli davrning oxirida bank qancha pul sarflaganingizni hisoblab chiqadi va sizga ko'chirma yuboradi",
                                         reply_markup=inline_builder(
                                             ['📅 +15 kun', "📌 To'lov vaqti", 'Ortga qaytish ↩️'],
                                             ['uz_fifteen', 'uz_payment_time', 'uz_back_to_card_from_grace'],
                                             [2, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>Xaridlaringiz uchun 30 kun</b>\n\nSiz kredit kartadan istalgan xaridlaringiz uchun 30 kun ichida pul sarflashingiz mumkin, har imtiyozli davrning oxirida bank qancha pul sarflaganingizni hisoblab chiqadi va sizga ko'chirma yuboradi",
                                      reply_markup=inline_builder(
                                          ['📅 +15 kun', "📌 To'lov vaqti", 'Ortga qaytish ↩️'],
                                          ['uz_fifteen', 'uz_payment_time', 'uz_back_to_card_from_grace'],
                                          [2, 1]
                                     )
        )
        await callback.answer()


# ------------------------------"30 kun" VA "To'lov vaqtidagi" DAGI "+15 kun" KNOPKASI------------------------------
@uz_user_router.callback_query(F.data == 'uz_fifteen')
async def uz_fifteen(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>To'lov uchun qo'shimcha 15 kun</b>\n\nQarzdorlikni to'lash uchun sizda yana 15 kun qoladi\n\nMasalan, ko'chirma sanasi 5 avgust, birinchi xarid 14 avgustda amalga oshirilgan, ikkinchisi esa — 25 avgustda\n\nXarajatlaringiz ko'rsatilgan ko'chirma sanasi 5 sentyabr, agar siz 20 sentyabrgacha (5 avgust + 45 kun) sarflangan mablag'ni to'liq qaytarsangiz, foizlar olinmaydi va ortiqcha to'lashingiz kerak bo'lmaydi\n\nKo'chirmada ko'rsatilgan qarzni to'lash vaqtida, siz kartadan foydalanishni davom ettirishingiz mumkin\n\nKo'chirma sanasining keyingi kunidan boshlab qilingan xarajatlar, birinchi imtiyozli davr uchun to'liq to'lov 15 kun ichida amalga oshirilishi sharti bilan yangi imtiyozli davrga o'tadi\n\nShunday qilib, ko'chirmani olgan kuningiz birinchi imtiyozli davr tugaydi va ertasi kuni esa yangi xaridlar uchun boshqa imtiyozli davr boshlanadi",
                                         reply_markup=inline_builder(
                                             ['📅 30 kun', "📌 To'lov vaqti", 'Ortga qaytish ↩️'],
                                             ['uz_thirty', 'uz_payment_time', 'uz_back_to_card_from_grace'],
                                             [2, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>To'lov uchun qo'shimcha 15 kun</b>\n\nQarzdorlikni to'lash uchun sizda yana 15 kun qoladi\n\nMasalan, ko'chirma sanasi 5 avgust, birinchi xarid 14 avgustda amalga oshirilgan, ikkinchisi esa — 25 avgustda\n\nXarajatlaringiz ko'rsatilgan ko'chirma sanasi 5 sentyabr, agar siz 20 sentyabrgacha (5 avgust + 45 kun) sarflangan mablag'ni to'liq qaytarsangiz, foizlar olinmaydi va ortiqcha to'lashingiz kerak bo'lmaydi\n\nKo'chirmada ko'rsatilgan qarzni to'lash vaqtida, siz kartadan foydalanishni davom ettirishingiz mumkin\n\nKo'chirma sanasining keyingi kunidan boshlab qilingan xarajatlar, birinchi imtiyozli davr uchun to'liq to'lov 15 kun ichida amalga oshirilishi sharti bilan yangi imtiyozli davrga o'tadi\n\nShunday qilib, ko'chirmani olgan kuningiz birinchi imtiyozli davr tugaydi va ertasi kuni esa yangi xaridlar uchun boshqa imtiyozli davr boshlanadi",
                                      reply_markup=inline_builder(
                                          ['📅 30 kun', "📌 To'lov vaqti", 'Ortga qaytish ↩️'],
                                          ['uz_thirty', 'uz_payment_time', 'uz_back_to_card_from_grace'],
                                          [2, 1]
                                     )
        )
        await callback.answer()


# --------------------------------"30 kun" VA "+15 kun" DAGI "To'lov vaqti" KNOPKASI--------------------------------
@uz_user_router.callback_query(F.data == 'uz_payment_time')
async def uz_payment_time(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>Xaridni qancha oldin amalga oshirsangiz, to'lov uchun shuncha ko'p vaqt bo'ladi</b>\n\nHar bir xaridingiz uchun imtiyozli davrning davomiyligi xaridni imtiyozli davrning qaysi kunida amalga oshirganingizga bog'liq\n\nMasalan, siz 45 kungacha imtiyozli davrga ega AVO platinum kredit kartasidan foydalanasiz. Ko'chirma sanasi har oyning 5-kuni\n\nAgar siz 6 avgust kuni xaridni amalga oshirsangiz — ko'chirma sanasidan keyingi kun — sizda ushbu xarid uchun 30 kunlik imtiyozli davr bo'ladi, pulni qaytarish uchun esa yana qo'shimcha 15 kun qoladi",
                                         reply_markup=inline_builder(
                                             ['📅 +15 kun', "📅 30 kun", 'Ortga qaytish ↩️'],
                                             ['uz_fifteen', 'uz_thirty', 'uz_back_to_card_from_grace'],
                                             [2, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>Xaridni qancha oldin amalga oshirsangiz, to'lov uchun shuncha ko'p vaqt bo'ladi</b>\n\nHar bir xaridingiz uchun imtiyozli davrning davomiyligi xaridni imtiyozli davrning qaysi kunida amalga oshirganingizga bog'liq\n\nMasalan, siz 45 kungacha imtiyozli davrga ega AVO platinum kredit kartasidan foydalanasiz. Ko'chirma sanasi har oyning 5-kuni\n\nAgar siz 6 avgust kuni xaridni amalga oshirsangiz — ko'chirma sanasidan keyingi kun — sizda ushbu xarid uchun 30 kunlik imtiyozli davr bo'ladi, pulni qaytarish uchun esa yana qo'shimcha 15 kun qoladi",
                                      reply_markup=inline_builder(
                                          ['📅 +15 kun', "📅 30 kun", 'Ortga qaytish ↩️'],
                                          ['uz_fifteen', 'uz_thirty', 'uz_back_to_card_from_grace'],
                                          [2, 1]
                                     )
        )
        await callback.answer()



# ---------------------------------------------"Operatsiyalar" KNOPKASI---------------------------------------------
@uz_user_router.callback_query(F.data.in_({'uz_operations', 'uz_back_to_operations_from_other_tariffs'}))
async def uz_operations(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Pul yechib olish va o'tkazmalar</b>\n\n• <b>Shaxsiy mablag'lar</b> hisobidan naqd pul yechib olish yoki kartalarga pul o'tkazish:\n- bepul, AVO mobil ilovasida va bankomatlarida\n- boshqa bank qurilmalari orqali operatsiya summasidan 0,5%\n• <b>Kredit mablag'lari</b> hisobidan naqd pul yechib olish yoki kartalarga pul o'tkazish:\n- 29 000 so'm + operatsiya summasidan 2,9%\n• O'tkazmalar va naqd pul yechib olish limiti:\n- <b>AVO platinum</b> kartasi bo'yicha — har bir operatsiya uchun 5 000 000 so'm, oyiga esa 50 000 000 so'm\n- <b>boshqa bank kartalari uchun</b> — har bir operatsiya uchun 5 000 000 so'm, oyiga esa 50 000 000 so'm\n• <b>Shaxsiy mablag'lar</b> hisobidan to'lovlar:\n- bepul, AVO mobil ilovasida\n• <b>Kredit mablag'lari</b> hisobidan to'lovlar:\n- bepul <i>(imtiyozsiz operatsiyalar bundan mustasno)</i>, AVO mobil ilovasida",
                                     reply_markup=inline_builder(
                                         ['📑 Boshqa tariflar', 'Ortga qaytish ↩️'],
                                         ['uz_other_tariffs_1', 'uz_back_to_main_from_operations']
                                    )
    )
    await callback.answer()


# ------------------"Operatsiyalar" DAGI "Boshqa tariflar" VA "Sahifa 2" DAGI "Sahifa 1" KNOPKASI------------------
@uz_user_router.callback_query(F.data == 'uz_other_tariffs_1')
async def uz_other_tariffs_1(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>AVO Bankga aloqador xizmatlar</b>\n\n<b>• AVO bankomatlarida AVO platinum kartasidagi balansni tekshirish:</b>\n- bepul <i>(boshqa bank bankomatlarida — 11 000 so'm)</i>\n<b>• Mobil ilovada, kontakt-markazga telefon qilish orqali AVO platinum kartasidagi balansni tekshirish:</b>\n- bepul\n<b>• 3D-Secure xizmati:</b>\n- bepul\n<b>• Kartani xalqaro stop-list ro'yxatiga kiritish:</b>\n- 150 000 so'm\n<b>• SMS/PUSH xabarnoma:</b>\n- oyiga 11 900 so'm",
                                     reply_markup=inline_builder(
                                         ['Sahifa 2 ➡️', 'Ortga qaytish ↩️'],
                                         ['uz_other_tariffs_2', 'uz_back_to_operations_from_other_tariffs']
                                    )
    )
    await callback.answer()


# ---------------------------------------"Sahifa 1" DAGI "Sahifa 2" KNOPKASI---------------------------------------
@uz_user_router.callback_query(F.data == 'uz_other_tariffs_2')
async def uz_other_tariffs_2(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Boshqa banklarning kartalariga xizmat ko'rsatish</b>\n\n<b>• AVO bankomati va mobil ilovasida amalga oshiriladigan to'lovlar:</b>\n- bepul <i>(komissiya olingan taqdirda, komissiya miqdori operatsiyani amalga oshirish vaqtida belgilanadi)</i>\n<b>• AVO bankomatlaridan naqd pul yechib olish:</b>\n- operatsiya summasidan 1%\n<b>• Kartani AVO bankomatlarida to'ldirish:</b>\n- operatsiya summasidan 0,5%\n<b>• AVO mobil ilovasi va bankomatlarida amalga oshiriladigan pul o'tkazmalari uchun komissiya:</b>\n- boshqa banklarning kartalari orqali amalga oshirilsa — 3 000 000 so'mgacha bepul, 3 000 000 so'mdan yuqori bo'lgan summa uchun — 0,5%\n<b>• AVO bankomatlarida karta balansini tekshirish:</b>\n- 11 000 so'm\n<b>• AVO bankomati va mobil ilovasida konvertatsiya qilish</b>\n- bank kursi + operatsiya summasidan 3%",
                                     reply_markup=inline_builder(
                                         ['Sahifa 1 ⬅️', 'Ortga qaytish ↩️'],
                                         ['uz_other_tariffs_1', 'uz_back_to_operations_from_other_tariffs']
                                    )
    )
    await callback.answer()


# ---------------------------------------------"Biz haqimizda" KNOPKASI---------------------------------------------
@uz_user_router.callback_query(F.data.in_({'uz_about_us', 'uz_back_to_about_us_from_documents'}))
async def uz_about_us(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer_photo(photo=img.about_us_uz_photo,
                                        caption="<b>Qadriyatlar</b>\n\nBizning qadriyatlarimiz bizning shaxsiyatimizni shakllantiradi va harakat tarzimizni belgilaydi\n✅ <b>Vijdon bilan</b>\n       Va'dalarni bajaramiz\n✅ <b>Qiziquvchanlik</b>\n       Biz doimo yangi yechimlarni qidiramiz va barcha fikr-mulohazalarni eshitamiz\n✅ <b>Oson</b>\n       Hamma uchun oson va tushunarli\n\n<b>Bizning maqsadimiz — mijozlarimiz hayotini yaxshilash</b>Biz, mijozlarmiz o'zlarini erkin, dadil va zamon bilan hamnafas bo'lishlari, hamda ertagi kunga ishonch bilan qarashlari sari intilamiz\n\nUshbu maqsadlarga erishish yo'lida, biz mijozlarimiz hayotlarini yanada yaxshilashga yordam beradigan, yuqori sifatli mahsulot va xizmatlarni taklif qilamiz\n\n<b>AVO — bu \"havo\" so'zining qisqartmasi</b>\nHavo yengil va toza bo'lganidek, biz taqdim etadigan moliyaviy xizmatlar ham kundalik foydalanishda qulay, tushunarli va oson",
                                        reply_markup=inline_builder(
                                            ['📃 Hujjatlar', 'Ortga qaytish ↩️'],
                                            ['uz_documents', 'uz_back_to_main_from_about_us']
                                        )
    )
    await callback.answer()


# -----------------------------------"Biz haqimizda" DAGI "Hujjatlar" KNOPKASI-------------------------------------
@uz_user_router.callback_query(F.data.in_({'uz_documents', 'uz_back_to_documents_from_for_clients', 'uz_back_to_documents_from_main_documents', 'uz_back_to_documents_from_important_facts', 'uz_back_to_documents_from_internal_regulatory_documents', 'uz_back_to_documents_from_affylated_persons', 'uz_back_to_documents_from_application_form', 'uz_back_to_documents_from_financial_statements', 'uz_back_to_documents_from_audit_reports', 'uz_back_to_documents_from_dividends'}))
async def uz_documents(callback: CallbackQuery) -> None:
    try:
        await callback.message.edit_text("<b>Hujjatlar va litsenziyalar</b>\n\nQuyidagilardan birini tanlab, hujjatlar bilan tanishib chiqishingiz mumkin 👇",
                                         reply_markup=inline_builder(
                                             ['📒 Mijozlar uchun', '📒 Asosiy hujjatlar', '📒 Muhim faktlar', '📒 Ichki normativ hujjatlar', '📒 Afillangan shaxslar', '📒 Murojaatlar shakli', '📒 Moliyaviy hisobotlar', '📒 Auditorlik hisobotlari', '📒 Dividendlar', 'Ortga qaytish ↩️'],
                                             ['uz_for_clients', 'uz_main_documents', 'uz_important_facts_1', 'uz_internal_regulatory_documents_1', 'uz_affylated_persons', 'uz_application_form', 'uz_financial_statements', 'uz_audit_reports', 'uz_dividends', 'uz_back_to_about_us_from_documents'],
                                             [2, 2, 2, 2, 1, 1]
                                        )
        )
        await callback.answer()
    except TelegramBadRequest:
        await callback.message.delete()
        await callback.message.answer("<b>Hujjatlar va litsenziyalar</b>\n\nQuyidagilardan birini tanlab, hujjatlar bilan tanishib chiqishingiz mumkin 👇",
                                      reply_markup=inline_builder(
                                          ['📒 Mijozlar uchun', '📒 Asosiy hujjatlar', '📒 Muhim faktlar', '📒 Ichki normativ hujjatlar', '📒 Afillangan shaxslar', '📒 Murojaatlar shakli', '📒 Moliyaviy hisobotlar', '📒 Auditorlik hisobotlari', '📒 Dividendlar', 'Ortga qaytish ↩️'],
                                          ['uz_for_clients', 'uz_main_documents', 'uz_important_facts_1', 'uz_internal_regulatory_documents_1', 'uz_affylated_persons', 'uz_application_form', 'uz_financial_statements', 'uz_audit_reports', 'uz_dividends', 'uz_back_to_about_us_from_documents'],
                                          [2, 2, 2, 2, 1, 1]
                                     )
        )
        await callback.answer()


# -----------------------------------"Hujjatlar" DAGI "Mijozlar uchun" KNOPKASI-------------------------------------
@uz_user_router.callback_query(F.data == 'uz_for_clients')
async def uz_for_clients(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Mijozlar uchun</b>\n\n📄 <a href='https://docs.avo.uz/AVO_dkbo_uz.pdf'>Kompleks bank xizmatlarini ko'rsatish shartlari (29.04.2024 dan boshlab amal qiladi)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_loyalty_uz.pdf'>AVO bank AJning sodiqlik dasturining umumiy shartlari (29.03.2024 dan boshlab amal qiladi)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_referral_uz.pdf'>«Do'stingizni kredit kartaga chorlang» aksiyasi qoidalari (29.03.2024 dan boshlab amal qiladi)</a>\n\n📄 <a href='https://docs.avo.uz/AVO_user_agreement_uz.pdf'>Foydalanuvchi kelishuvi</a>\n\n📄 <a href='https://docs.avo.uz/AVO_consent_form_uz.pdf'>Shaxsiy ma'lumotlarni qayta ishlash uchun rozilik va kredit byurosidan kredit hisobotini olish shakli</a>\n\n📄 <a href='https://docs.avo.uz/AVO_privacy_policy_web_uz.pdf'>Maxfiylik siyosati</a>\n\n📄 <a href='https://docs.avo.uz/AVO_tariffs_uz.pdf'>Tariflar</a>\n\n📄 <a href='https://docs.avo.uz/AVO_bank_partners_uz.pdf'>Bank hamkorlari</a>\n\n📄 <a href='https://docs.avo.uz/AVO_rules_for_using_ATMs_uz.pdf'>AVO bankomatlaridan foydalanish qoidalari</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_for_clients']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ----------------------------------"Hujjatlar" DAGI "Asosiy hujjatlar" KNOPKASI------------------------------------
@uz_user_router.callback_query(F.data == 'uz_main_documents')
async def uz_main_documents(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Asosiy hujjatlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_Article_of_Association_ru.pdf'>Bank ustavi</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Banking_License_ru.pdf'>Litsenziya</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Amendments_to_the_Articles_of_Association_ru.pdf'>Bank ustaviga o'zgartirishlar №1</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Amendments_to_the_Articles_of_Association_240329_ru.pdf'>Bank ustaviga o'zgartirishlar №2</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_main_documents']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------"Hujjatlar" DAGI "Muhim faktlar" VA "Sahifa 2" DAGI "Sahifa 1" KNOPKASI---------------------
@uz_user_router.callback_query(F.data == 'uz_important_facts_1')
async def uz_important_facts_1(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Muhim faktlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.06_6.pdf'>Muhim fakt №6, 06.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.16_21.pdf'>Muhim fakt №21, 16.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.16_6.pdf'>Muhim fakt №6, 16.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.19_8.pdf'>Muhim fakt №8, 19.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.19_21_2.pdf'>Muhim fakt №21, 19.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.22_36.pdf'>Muhim fakt №36, 22.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.01.22_21.pdf'>Muhim fakt №21, 22.01.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.02.02_6.pdf'>Muhim fakt №6, 02.02.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.02.02_8.pdf'>Muhim fakt №8, 02.02.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material%20fact_24.02.28_6.pdf'>Muhim fakt №6, 28.02.2024</a>",
                                     reply_markup=inline_builder(
                                         ['Sahifa 2 ➡️', 'Ortga qaytish ↩️'],
                                         ['uz_important_facts_2', 'uz_back_to_documents_from_important_facts']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Sahifa 1" DAGI "Sahifa 2" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_important_facts_2')
async def uz_important_facts_2(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Muhim faktlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_material%20fact_24.02.28_36.pdf'>Muhim fakt №36, 28.02.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material%20fact_24.03.20_6.pdf'>Muhim fakt №6, 20.03.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.04.25_21.pdf'>Muhim fakt №21, 25.04.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.05.14_6.pdf'>Muhim fakt №21, 14.05.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.05.22_6.pdf'>Muhim fakt №6, 22.05.2024</a>\n\n📄 <a href='https://docs.avo.uz/AVO_material_fact_24.05.22_2.pdf'>Muhim fakt №2, 22.05.2024</a>",
                                     reply_markup=inline_builder(
                                         ['Sahifa 1 ⬅️', 'Ortga qaytish ↩️'],
                                         ['uz_important_facts_1', 'uz_back_to_documents_from_important_facts']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ----------------"Hujjatlar" DAGI "Ichki normativ hujjatlar" VA "Sahifa 2" DAGI "Sahifa 1" KNOPKASI------------------
@uz_user_router.callback_query(F.data == 'uz_internal_regulatory_documents_1')
async def uz_internal_regulatory_documents_1(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Ichki normativ hujjatlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_corporate_governance_policy_ru.pdf'>Korporativ boshqaruv siyosati</a>\n\n📄 <a href='https://docs.avo.uz/AVO_Regulations_Sole_Shareholder_ru.pdf'>Yuqori boshqaruv organi (yagona Aksiyador) to'g'risidagi nizom</a>\n\n📄 <a href='https://docs.avo.uz/AVO_supervisory_board_ru.pdf'>Kuzatuv kengashi to'g'risidagi nizom</a>\n\n📄 <a href='https://docs.avo.uz/AVO_executive_board_ru.pdf'>Ijro etuvchi organ (boshqaruv) to'g'risidagi nizom</a>\n\n📄 <a href='https://docs.avo.uz/AVO_internal_audit_service_ru.pdf'>Ichki audit xizmati to'g'risidagi nizom</a>\n\n📄 <a href='https://docs.avo.uz/AVO_conflict_of_interest_policy_ru.pdf'>Manfaatlar to'qnashuvining oldini olish va tartibga solish siyosati</a>\n\n📄 <a href='https://docs.avo.uz/AVO_disclosure_policy_ru.pdf'>Axborotni oshkor qilish siyosati</a>\n\n📄 <a href='https://docs.avo.uz/AVO_dividend_policy_ru.pdf'>Dividendlarni to'lash siyosati</a>\n\n📄 <a href='https://docs.avo.uz/AVO_business_plan_and_development_strategy_ru.pdf'>Biznes-reja va Rivojlanish strategiyasi</a>\n\n📄 <a href='https://docs.avo.uz/AVO_bank_regulations_ru.pdf'>Jismoniy va yuridik shaxslarning murojaatlarini ko'rib chiqish tartibi to'g'risidagi nizom</a>",
                                     reply_markup=inline_builder(
                                         ['Sahifa 2 ➡️', 'Ortga qaytish ↩️'],
                                         ['uz_internal_regulatory_documents_2', 'uz_back_to_documents_from_internal_regulatory_documents']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Sahifa 1" DAGI "Sahifa 2" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_internal_regulatory_documents_2')
async def uz_internal_regulatory_documents_2(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Ichki normativ hujjatlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_Corporate_Ethics_Code_ru.pdf'>Korporativ etika kodeksi</a>",
                                     reply_markup=inline_builder(
                                         ['Sahifa 1 ⬅️', 'Ortga qaytish ↩️'],
                                         ['uz_internal_regulatory_documents_1', 'uz_back_to_documents_from_internal_regulatory_documents']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Hujjatlar" DAGI "Afillangan shaxslar" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_affylated_persons')
async def uz_affylated_persons(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Afillangan shaxslar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_affiliates.pdf'>Afillangan shaxslar ro'yxati</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_affylated_persons']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Hujjatlar" DAGI "Murojaatlar shakli" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_application_form')
async def uz_application_form(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Murojaatlar shakli</b>\n\n📄 <a href='https://docs.avo.uz/Antifraud_form_uz.pdf'>Mijozning antifrod tizimi bo'yicha so'rovini qabul qilish shakli</a>\n\n📄 <a href='https://avo.uz/contract-termination'>Shartnomani bekor qilish bo'yicha qo'llanma</a>\n\n📄 <a href='https://docs.avo.uz/application_for_disput_uz.pdf'>Muammoli operatsiyalarni yechish uchun ariza</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_application_form']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Hujjatlar" DAGI "Moliyaviy hisobotlar" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_financial_statements')
async def uz_financial_statements(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Moliyaviy hisobotlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_financial_statements.pdf'>2023-yil uchun yillik hisobot</a>\n\n📄 <a href='https://docs.avo.uz/AVO_first_quartile.pdf'>2024-yil 1-chorak yakunlari bo'yicha hisobot</a>\n\n📄 <a href='https://docs.avo.uz/AVO_first_quartile_emitter.pdf'>2024-yil 1-chorak yakunlari bo'yicha emitent hisoboti</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_financial_statements']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Hujjatlar" DAGI "Auditorlik hisobotlari" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_audit_reports')
async def uz_audit_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Auditorlik hisobotlari</b>\n\n📄 <a href='https://docs.avo.uz/AVO_financial_statements.pdf'>2023-yil uchun yillik hisobot</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_audit_reports']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()


# ---------------------------------------"Hujjatlar" DAGI "Dividendlar" KNOPKASI-----------------------------------------
@uz_user_router.callback_query(F.data == 'uz_dividends')
async def uz_dividends(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Dividendlar</b>\n\n📄 <a href='https://docs.avo.uz/AVO_dividend_payment_uz.pdf'>Oxirgi 3 yil ichida taqsimlangan va to'langan dividendlar</a>",
                                     reply_markup=inline_builder(
                                         ['Ortga qaytish ↩️'],
                                         ['uz_back_to_documents_from_dividends']
                                     ),
                                     disable_web_page_preview=True
    )
    await callback.answer()
