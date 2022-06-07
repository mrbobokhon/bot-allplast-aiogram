import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import sqlite3
TOKEN = "1932309117:AAFzb5NsmX0bugbcPoN6pn9e0X-EvdJaLAs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, '🇺🇿Assalomu aleykum {0.first_name} olplasofficialbotga xush kelibsiz!\n\n🇷🇺Здравствуйте {0.first_name} добро пожаловать в olplasofficialbot'.format(message.from_user), reply_markup = nav.mainMenu)
    await bot.send_message(message.from_user.id, 'Tillni tanlang!\nВыберите язык!'.format(message.from_user), reply_markup = nav.mainMenu)
    
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
        )""")

    connect.commit()

    user_id = [message.chat.id]
    cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
    connect.commit()
    

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '🇷🇺Rus':
        await bot.send_message(message.from_user.id, 'Вы выбрали русский 🇷🇺язык', reply_markup = nav.mainproduct2)

    elif message.text == '🇺🇿Uzb':
        await bot.send_message(message.from_user.id, 'Siz 🇺🇿Uzb tilini tanladingiz', reply_markup = nav.mainproduct)

    elif message.text == '🔹 Mavjud maxsulotlar royxati':
        await bot.send_message(message.from_user.id, "Bizda mavjud maxsulotlar ro'yxati", reply_markup = nav.otherMenu)
    
    elif message.text == '🔹 Bosh menyuga qaytish':
        await bot.send_message(message.from_user.id, 'Bosh menyu', reply_markup = nav.mainMenu)
    
    elif message.text == '🔹 Poliproplien qop':
        await bot.send_message(message.from_user.id,"Poliproplien qoplarning ro'yxati", reply_markup = nav.polipropilen)

    elif message.text == '🔹 Skotch':
        await message.reply("Telefon raqamingiz +998.. kodi bilan kiriting\nFirmangiz nomini firma deb kiriting va bizning operatorlarimiz siz bilan tez orada bog'lanishadi!")

    elif message.text == '🔹 Politelen paket':
        await message.reply("Telefon raqamingiz +998.. kodi bilan kiriting\nFirmangiz nomini firma deb kiriting va bizning operatorlarimiz siz bilan tez orada bog'lanishadi!")

    elif message.text == '🔹 Yevro qop':
        await message.reply("Narxni bilish uchun o'lchamni kiriting\n Masalan \n10 * 20\n5 * 10,\n3 * 8")
    
    elif message.text == '🔹 Un uchun':
        await message.reply("Narxni bilish uchun o'lchamni kiriting\n Masalan \n50*80\n55*105,\n80*140")

    elif message.text == '🔹 Yem uchun':
        await message.reply("Narxni bilish uchun o'lchamni kiriting\n Masalan \n50*80\n55*105,\n80*140")

    elif message.text == '🔹 Tekstillar uchun':
        await message.reply("Narxni bilish uchun o'lchamni kiriting\n Masalan \n50*80\n55*105,\n80*140")
    
    elif "*" in message.text:
        await message.reply("Endi esa qopning gramini kiriting")
        

    elif "-" in message.text:
        await message.reply("Теперь введите грамм мешка!")
    
    elif message.text == '📞 Свяжитесь с нами' or message.text == "📞 Biz bilan bog'lanish":
        await message.reply("Number:+998997808001\n+998997808000\nE-mail: sh.hudoyberdiev@uztex.uz")


# ------------ Russian language ------------ #

    elif message.text == '🔹 Список доступных продуктов':
        await bot.send_message(message.from_user.id, "Список доступных продуктов", reply_markup = nav.otherMenu2)
    
    elif message.text == '🔹 Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)
    
    elif message.text == '🔹 Мешок полипропиленовый':
        await bot.send_message(message.from_user.id,"Список полипропиленовых мешков", reply_markup = nav.polipropilen2)

    elif message.text == '🔹 Скотч':
        await message.reply("Введите свой номер телефона с кодом +998 .. \nВведите название вашей компании в качестве firma например firma olplast, и наши операторы свяжутся с вами в ближайшее время.")

    elif message.text == '🔹 Полиэтиленовый пакет':
        await message.reply("Введите свой номер телефона с кодом +998 .. \nВведите название вашей компании в качестве firm например firma olplast, и наши операторы свяжутся с вами в ближайшее время.")

    elif message.text == '🔹 Евро':
        await message.reply("Введите размер, чтобы узнать цену\n Например, \n50-80\n55-105,\n80-140")
    
    elif message.text == '🔹 Для муки':
        await message.reply("Введите размер, чтобы узнать цену\n Например, \n50-80\n55-105,\n80-140")

    elif message.text == '🔹 Для корма':
        await message.reply("Введите размер, чтобы узнать цену\n Например, \n50-80\n55-105,\n80-140")

    elif message.text == '🔹 Для текстиля':
        await message.reply("Введите размер, чтобы узнать цену\n Например, \n50-80\n55-105,\n80-140")
    
    elif '+998' in message.text:
        await message.reply("☑️")

        connect = sqlite3.connect("users.db")
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login_number(
            id TEXT NOT NULL
            )""")

        connect.commit()

        user_id = [message.text]
        cursor.execute("INSERT INTO login_number VALUES(?);", user_id)
        connect.commit()
        

    elif 'firm' in message.text.lower():
        await message.reply("☑️")

        connect = sqlite3.connect("users.db")
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login_firma(
            id TEXT NOT NULL
            )""")

        connect.commit()

        user_id = [message.text]
        cursor.execute("INSERT INTO login_firma VALUES(?);", user_id)
        connect.commit()
        

    elif message.text.lower() > "a" and message.text < "z":
        await message.reply("sorry!")
        
    elif int(message.text) >= 30 and int(message.text) <= 500:
        a = int(message.text) * 30
        await message.reply(str(a) +"So'm")
        # await bot.send_message("Ismingiz\nTelefon raqamingiz\nFirmangiz nomini kiriting va bizning operatorlarimiz siz bilan tez orada bog'lanishadi!")
        
    else:
        await message.reply("Sorry!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)