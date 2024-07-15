from aiogram import types
import wikipedia
from loader import dp

wikipedia.set_lang("uz")


@dp.message_handler()
async def bot_start(message: types.Message):
    text = message.text
    result = wikipedia.summary(f"{text}", sentences=6)
    await message.answer(result)