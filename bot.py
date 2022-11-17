from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN, ID


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Доброго времени суток! Этот бот нужен для обратной связи! Или можешь узнать свой ID по команде /id")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id, "Команда для ответа пользователям:\n/answer id message\n\nУзнать свой ID:\n/id")
    else:
        await bot.send_message(message.from_user.id, "Доброго времени суток! Этот бот нужен для обратной связи! Или можешь узнать свой ID по команде /id")


@dp.message_handler(commands=['id'])
async def process_id_command(message: types.Message):
    await bot.send_message(message.from_user.id, message.from_user.id)


@dp.message_handler(commands=['answer'])
async def answer_message(message: types.Message):
    if message.from_user.id == ID:
        text = message.text[8:]
        for i in range(14):
            if text[:i].isdigit():
                id = text[:i]
                k = i
        await bot.send_message(id, text[k:])
    else:
        id = 'ID: ' + str(message.from_user.id)
        username = 'Username: ' + str(message.from_user.username)
        text = id + '\n' + username + '\n\n' + 'Text: ' + str(message.text)
        await bot.send_message(ID, text)


@dp.message_handler()
async def echo_message(message: types.Message):
    id = 'ID: ' + str(message.from_user.id)
    username = 'Username: ' + str(message.from_user.username)
    text = id + '\n' + username + '\n\n' + 'Text: ' + str(message.text)
    await bot.send_message(ID, text)
    await message.reply("Спасибо за обратную связь!")


if __name__ == '__main__':
    executor.start_polling(dp)