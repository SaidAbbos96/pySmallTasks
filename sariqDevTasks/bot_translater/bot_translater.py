from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from translater import translater

# bu yerga token kiritamiz
TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Assalom alaykum, {message.from_user.username} Kirill-Lotin-Kirill botiga xush kelibsiz!\nMatningizni yuboring.')


@dp.message_handler()
async def transleter(msg: types.Message):
    await bot.send_message(msg.from_user.id, translater(msg.text))

# botni ishga tushuramiz
if __name__ == '__main__':
    executor.start_polling(dp)
