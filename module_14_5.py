import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import texts14
from crud_functions import is_included, add_user
import crud_functions

def get_all_products():
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id, title, description, price, image_path FROM Products')
        return cursor.fetchall()


# Инициализация бота и диспетчера
bot = Bot(token='7777')
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text='Рассчитать')
button5 = KeyboardButton(text='Купить')
button1 = KeyboardButton(text='Регистрация')
kb.row(button, button2)
kb.row(button1, button5)

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

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

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


@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sign_up(message: types.Message, state: FSMContext):
    # Устанавливаем состояние для ввода имени пользователя
    await RegistrationState.username.set()
    await message.answer('Введите свое имя: (только латинский алфавит)')


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    if is_included(message.text):  # Проверяем, существует ли пользователь
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
        return

    # Сохраняем имя пользователя
    async with state.proxy() as data:
        data['username'] = message.text

    await RegistrationState.email.set()
    await message.answer("Введите свой email:")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await RegistrationState.age.set()
    await message.answer("Введите свой возраст:")


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

        # Получаем все данные и добавляем пользователя
        add_user(
            username=data['username'],
            email=data['email'],
            age=data['age']
        )

    await message.answer("Регистрация успешно завершена!\n "
                         "Нажмите 'Рассчитать' для расчета нормы калорий",
                         reply_markup=kb)
    await state.finish()

@dp.message_handler(text='Информация')
async def info(message:types.Message):
    with open('files/prods.png', 'rb') as img:
        await message.answer_photo(img, texts14.about)
        await message.answer('Нажмите "Купить" для приобретения', reply_markup=kb)

@dp.message_handler(text="Купить")
async def show_catalog(message: types.Message):
    products = get_all_products()
    for product in products:
        id, title, description, price, image_path = product
        await message.answer_photo(
            photo=open(image_path, 'rb'),
            caption=f"Товар: {title}\n"
                    f"Описание: {description}\n"
                    f"Цена: {price} руб."
            )

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
                         'Нажмите кнопку "Регистрация" ',
                         reply_markup=kb)

@dp.message_handler(lambda message: message.text not in['/start', 'Информация', 'Рассчитать', 'Купить'])
async def first_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение ')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
