import os
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6715751133:AAFnqBhs_ZeW8Vrz3E3x-OKOVIWzrwjP4zM")
dp = Dispatcher(bot)

sticker_folder_path = r"./"

sticker_files = [f for f in os.listdir(sticker_folder_path) if os.path.isfile(os.path.join(sticker_folder_path, f))]

@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Рандомное число")],
        [types.KeyboardButton(text="Рандомный стикер")],
        [types.KeyboardButton(text="Что-то")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Привет, я бот в тг", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Рандомный стикер")
async def process_random_sticker(message: types.Message):
    if sticker_files:
        random_sticker_file = random.choice(sticker_files)
        sticker_path = os.path.join(sticker_folder_path, random_sticker_file)
        with open(sticker_path, "rb") as sticker:
            await bot.send_sticker(message.from_user.id, sticker)
    else:
        await bot.send_message(message.from_user.id, "В папке нет фотографий стикеров.")

@dp.message_handler(lambda message: message.text == "Рандомное число")
async def process_random_number(message: types.Message):
    import random
    a = random.randint(1, 100)
    await bot.send_message(message.from_user.id, str(a))

@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    executor.start_polling(dp)