from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


# Инициализация бота и диспетчера
bot = Bot(token='7777')
dp = Dispatcher(bot, storage=MemoryStorage())


# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик команды start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью\nВведите слово "Calories" для расчета нормы калорий')

# Начало цепочки состояний
@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

# Обработка возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

# Обработка роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

# Обработка веса и финальный расчет
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        # Конвертируем строковые значения в числа
        age = float(data['age'])
        weight = float(data['weight'])
        height = float(data['growth'])

        # Формула Миффлина-Сан Жеора для женщин
        # BMR = (10 × вес в кг) + (6.25 × рост в см) - (5 × возраст) - 161
        calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

        await message.answer(f"Ваша суточная норма калорий: {round(calories)} ккал")

    finally:
        # Завершаем машину состояний
        await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


