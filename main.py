from aiogram import Bot, Dispatcher, types, F
from aiogram.types import UserProfilePhotos
from aiogram.filters.command import Command
from aiogram.filters import Filter
import asyncio


# Инициализация бота
bot = Bot(token='YOUR TOKEN')
# Диспетчер
dp = Dispatcher()


# Стартовая функция 
# Реагирует на /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет! Я бот для чего-то там)")


# Обработчик фото
@dp.message(F.photo)
async def get_photo(message: types.file):
    pass


# Обработчик сообщений
@dp.message(F.text)
async def message_handler(message: types.Message):
    msg = message.text.lower()

    if msg == 'тест':
        await message.answer(f"Работаю!")



# Обработчик callback кнопок
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "callback_data":
        pass


# Main функция
async def main():
    await dp.start_polling(bot)


# Запускаем цикл
if __name__ == "__main__":
    print("\nБот запущен\n")
    asyncio.run(main())
