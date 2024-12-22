from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

import config14
import texts14


# Инициализация бота и диспетчера
bot = Bot(token='7777692292:AAH0jbJOaWGlZlMQLheLdWn3yZp1xW2kFfs')
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text='Рассчитать')
button5 = KeyboardButton(text='Купить')
kb.row(button, button2)
kb.add(button5)

kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчет нормы для женщин', callback_data='calories for women')
button6 = InlineKeyboardButton(text='Рассчет нормы для мужчин', callback_data='calories for men')
button4 = InlineKeyboardButton(text='Формула для женщин', callback_data='formula for women')
button7 = InlineKeyboardButton(text='Формула для мужчин', callback_data='formula for men')

kb2.add(button3, button4)
kb2.add(button6, button7)

buy_kb = InlineKeyboardMarkup()
button8 = InlineKeyboardButton(text='Продукт1', callback_data='product_buying_1')
button9 = InlineKeyboardButton(text='Продукт2', callback_data='product_buying_2')
button10 = InlineKeyboardButton(text='Продукт3', callback_data='product_buying_3')
button11 = InlineKeyboardButton(text='Продукт4', callback_data='product_buying_4')

buy_kb.row (button8, button9, button10, button11)


# Определение состояний
class WomenState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class MenState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(lambda message: message.text =='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.callback_query_handler(text='formula for women')
async def show_women_formula(call: types.CallbackQuery):
    formula_text = (
        "Формула расчета BMR для женщин:\n\n"
        "BMR = (10 × вес в кг) + (6.25 × рост в см) - (5 × возраст) - 161\n\n"
        "Эта формула Миффлина-Сан Жеора позволяет рассчитать базовый уровень метаболизма."
    )
    await call.message.answer(formula_text)
    await call.answer()

@dp.callback_query_handler(text='formula for men')
async def show_men_formula(call: types.CallbackQuery):
    formula_text = (
        "Формула расчета BMR для мужчин:\n\n"
        "BMR = (10 × вес в кг) + (6.25 × рост в см) - (5 × возраст) + 5\n\n"
        "Эта формула Миффлина-Сан Жеора позволяет рассчитать базовый уровень метаболизма."
    )
    await call.message.answer(formula_text)
    await call.answer()


# Для женщин
@dp.callback_query_handler(text='calories for women')
async def set_age_women(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await WomenState.age.set()
    await call.answer()

@dp.message_handler(state=WomenState.age)
async def set_growth_women(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await WomenState.growth.set()

@dp.message_handler(state=WomenState.growth)
async def set_weight_women(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await WomenState.weight.set()

# Для мужчин
@dp.callback_query_handler(text='calories for men')
async def set_age_men(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await MenState.age.set()
    await call.answer()

@dp.message_handler(state=MenState.age)
async def set_growth_men(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await MenState.growth.set()

@dp.message_handler(state=MenState.growth)
async def set_weight_men(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await MenState.weight.set()

@dp.message_handler(state=WomenState.weight)
async def send_calories_women(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = float(data['age'])
        weight = float(data['weight'])
        height = float(data['growth'])

        # Формула для женщин
        calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

        await message.answer(f"Ваша базовая норма калорий (BMR): {round(calories)} ккал/день")
        await message.answer('Нажмите "Информация" для выбора продукта', reply_markup=kb )
        await state.finish()

    except ValueError:
        await message.answer("Пожалуйста, введите корректные числовые значения")
        await state.finish()

@dp.message_handler(state=MenState.weight)
async def send_calories_men(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = float(data['age'])
        weight = float(data['weight'])
        height = float(data['growth'])

        # Формула для мужчин
        calories = (10 * weight) + (6.25 * height) - (5 * age) + 5

        await message.answer(f"Ваша базовая норма калорий (BMR): {round(calories)} ккал/день")
        await message.answer('Нажмите "Информация" для выбора продукта', reply_markup=kb)
        await state.finish()

    except ValueError:
        await message.answer("Пожалуйста, введите корректные числовые значения")
        await state.finish()

    finally:
        # Завершаем машину состояний
        await state.finish()

@dp.message_handler(text='Информация')
async def info(message:types.Message):
    with open('files/photo8.png', 'rb') as img:
        await message.answer_photo(img, texts14.about)
        await message.answer('Нажмите "Купить" для приобретения', reply_markup=kb)


@dp.message_handler(lambda message: message.text == "Купить")
async def buy_command(message: types.Message):
    await get_buying_list(message)


async def get_buying_list(message: types.Message):
    from config14 import price1, price2, price3, price4
    from texts14 import product1, product2, product3, product4

    # Отправляем информацию о каждом продукте с фото
    await message.answer(product1)
    await message.answer_photo(photo=open('files/photo6.png', 'rb'))

    await message.answer(product2)
    await message.answer_photo(photo=open('files/photo7.png', 'rb'))

    await message.answer(product3)
    await message.answer_photo(photo=open('files/photo9.png', 'rb'))

    await message.answer(product4)
    await message.answer_photo(photo=open('files/photo10.png', 'rb'))

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('product_buying'))
async def process_buying(call: types.CallbackQuery):
    await send_confirm_message(call)

async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id, "Вы успешно приобрели продукт!")

@dp.message_handler(commands=['start'])
async def second_message(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью!\n'
                         'Нажмите кнопку "Рассчитать" для расчета нормы калорий',
                         reply_markup=kb)

@dp.message_handler(lambda message: message.text not in['/start', 'Информация', 'Рассчитать', 'Купить'])
async def first_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение ')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

