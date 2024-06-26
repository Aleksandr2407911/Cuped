from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message,
                           KeyboardButton, ReplyKeyboardMarkup, CallbackQuery, FSInputFile)
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


# Ответы для получения ключей
answers_for_key = {'key1': '1', 'key2': '2', 'key3': '3', 'key4': '4', 'key5': '5', 'key6': '6'}
keys = {'key1': '1', 'key2': '2', 'key3': '3', 'key4': '4', 'key5': '5', 'key6': '6'}

# Определяем состояние для бота
class UserState(StatesGroup):
    waiting_for_input = State()

# инициализируем роутер уровня модуля
router = Router()

# Создаем объект кнопок главного меню
button_1 = KeyboardButton(text='Ключи')
button_2 = KeyboardButton(text='Пойти на свидание с создателем')
button_3 = KeyboardButton(text='Поднять натстроние')
button_3 = KeyboardButton(text='Удалить бота')


# Создаем объект клавиатуры и добавляем кнопки главного меню
Keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3]], resize_keyboard=True)


button_key1 = InlineKeyboardButton(text='первый ключ', callback_data='button_key1')
button_key2 = InlineKeyboardButton(text='второй ключ', callback_data='button_key2')
button_key3 = InlineKeyboardButton(text='третий ключ', callback_data='button_key3')
button_key4 = InlineKeyboardButton(text='четвертый ключ', callback_data='button_key4')
button_key5 = InlineKeyboardButton(text='пятый ключ', callback_data='button_key5')
button_key6 = InlineKeyboardButton(text='шестой ключ', callback_data='button_key6')

keyboard_keys = InlineKeyboardMarkup(
    inline_keyboard=[[button_key1], [button_key2], [button_key3], [button_key4], [button_key5], [button_key6]]
)


@router.message(Command(commands= ['start']))
async def process_start_command(message: Message):
    await message.answer(text='Здесь будет описание бота с егэ функционалом', reply_markup=Keyboard)


@router.message(F.text == 'Ключи')
async def process_keys(message: Message):
    await message.answer(text='Список ключей', reply_markup=keyboard_keys)


@router.message(F.text == 'Пойти на свидание с создателем')
async def process_meeting(message: Message):
    await message.answer(text='пойти на свидание с создателем')


@router.message(F.text == 'Навсегда удалить бота')
async def process_delete(message: Message):
    await message.answer(text='Навсегда удалить бота')

@router.callback_query(F.data == "button_key1")
async def process_button_key1(state: FSMContext, message: Message):
    await message.answer("Для получения доступа к ключу введите ответ на вопрос")
    await state.set_state(UserState.waiting_for_input)

@router.message(UserState.waiting_for_input)
async def process_user_input_key1(message: Message, state: FSMContext):
    user_input = message.text
    if user_input == answers_for_key['key1']:
        await message.answer(f"Подзравляю вы ввели правильный ответ, ключ 1: {keys['key1']}")
        await state.clear
    else:
        await message.answer("Неправильный ответ")

