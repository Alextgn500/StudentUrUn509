from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Инициализация бота и диспетчера
bot = Bot(token='777')
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text='Рассчитать')
kb.row(button, button2)
kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb2.add(button3, button4)
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=
        [
            KeyboardButton(text='Рассчитать норму калорий', callbeck_data='calories'),
            KeyboardButton(text='Формулы расчета', callback_data='formulas')]
        )


# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(lambda message: message.text =='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    formula_text = "Формула Миффлина-Сан Жеора для женщин:\nBMR = (10 × вес в кг) + (6.25 × рост в см) - (5 × возраст) - 161"
    await call.message.answer(formula_text)


@dp.callback_query_handler(text='calories')
async def set_age(call: types.Message, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

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
    except ValueError:
        await message.answer("Пожалуйста, введите корректное числовое значение")

    finally:
        # Завершаем машину состояний
        await state.finish()

@dp.message_handler(commands='start')
async def second_message(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью!'
                         '\n''Нажмите кнопку "Рассчитать" для расчета нормы калорий',
                         reply_markup=kb)

@dp.message_handler(lambda message: message.text not in['/start', 'Информация', 'Рассчитать'])
async def first_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение ')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


