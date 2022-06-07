from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main Lenguage ---
btnRandom = KeyboardButton('🇷🇺Rus')
btnOther = KeyboardButton('🇺🇿Uzb')
# abc = KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)

# --- go back ---
btnMain = KeyboardButton('🔹 Bosh menyuga qaytish')
btnMain1 = KeyboardButton("📞 Biz bilan bog'lanish")

# --- Main ---
btnproduct = KeyboardButton('🔹 Mavjud maxsulotlar royxati')
mainproduct = ReplyKeyboardMarkup(resize_keyboard = True).add(btnproduct,btnMain).add(btnMain1)

# --- Menu Products ---
btnInfo = KeyboardButton('🔹 Poliproplien qop')
btnMoney = KeyboardButton('🔹 Politelen paket')
btnMoneys = KeyboardButton('🔹 Skotch')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMoney, btnMoneys, btnMain,btnMain1)


# --- Main Polipropen qoplar ---
btnun = KeyboardButton('🔹 Un uchun')
btnyem = KeyboardButton('🔹 Yem uchun')
btntekstil = KeyboardButton('🔹 Tekstillar uchun')
btnyevro = KeyboardButton('🔹 Yeuvro qop')
polipropilen = ReplyKeyboardMarkup(resize_keyboard = True).add(btnun, btnyem, btntekstil, btnyevro, btnMain,btnMain1)




# ---  Russian language --- 

# --- go back ---
btnMain2 = KeyboardButton('🔹 Главное меню')
btnMain3 = KeyboardButton('📞 Свяжитесь с нами')
# --- Main ---
btnproduct2 = KeyboardButton('🔹 Список доступных продуктов')
mainproduct2 = ReplyKeyboardMarkup(resize_keyboard = True).add(btnproduct2, btnMain2).add(btnMain3)

# --- Menu Products ---
btnInfo2 = KeyboardButton('🔹 Мешок полипропиленовый')
btnMoney2 = KeyboardButton('🔹 Полиэтиленовый пакет')
btnMoneys2 = KeyboardButton('🔹 Скотч')
otherMenu2 = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo2, btnMoney2, btnMoneys2, btnMain2,btnMain3 )


# --- Main Polipropen qoplar ---
btnun2 = KeyboardButton('🔹 Для муки')
btnyem2 = KeyboardButton('🔹 Для корма')
btntekstil2 = KeyboardButton('🔹 Для текстиля')
btnyevro2 = KeyboardButton('🔹 Евро')
polipropilen2 = ReplyKeyboardMarkup(resize_keyboard = True).add(btnun2, btnyem2, btntekstil2, btnyevro2, btnMain2,btnMain3 )
