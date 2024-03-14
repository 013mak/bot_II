
from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from Lesson1.Keyboards.keyboards import kb1
from Lesson1.Utils.random_fox import fox

router=Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


#Хэндлер на команду /stop
@router.message(F.text.lower()=='стоп')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Bye, {name}!', reply_markup=kb1)

#Хэндлер на команду /info
@router.message(F.text.lower()=='инфо')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Я - бот, работают 6 кнопок, 1 с сюрпризом. реагирую на слова: привет; эй ты; ты меня уважаешь? и ой все', reply_markup=kb1)

#Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower()=='покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Лови, {name}')
    await message.answer_photo(photo=img_fox)
#    await bot.send_photo(message.from_user.id)

#Хэндлер на команду /close
@router.message(F.text.lower()=='закрыть')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Ну ты эта, заходи если чо, {name}', reply_markup=kb1)

#Хэндлер на команду /anekdot
@router.message(F.text.lower()=='анекдот')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Сюрприз ) нету анекдотов', reply_markup=kb1)


#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Сам привет, {name}')
    elif 'эй ты' == msg_user:
        await message.answer(f'А вот хамить не надо')
    elif 'ты меня уважаешь?' in msg_user:
        await message.answer(f'Я тобой горжусь, {name}!!!')
    elif 'ой все' in msg_user:
        await message.answer(f'Ну не обижайся, {name}, давай попробуем еще раз')
    else:
        await message.answer(f'Моя твоя не понима')


