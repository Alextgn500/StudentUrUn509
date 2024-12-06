from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

async def on_startup(_):
    print('Бот успешно запущен')

async def on_shutdown(_):
    print('Бот остановлен')


api = '777'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print('Привет! Я бот, помогающий твоему здоровью')
    await message.answer('Привет! Я бот, помогающий твоему здоровью')

@dp.message_handler()
async def all_message(message: types.Message):
    print('Введите команду /start, чтобы начать общение')
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
        on_startup= on_startup, on_shutdown= on_shutdown)