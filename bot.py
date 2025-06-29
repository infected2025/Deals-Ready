import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from parser import parse_manomano

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(msg: types.Message):
    await msg.answer("Привет! Я Elvaro Deals Bot. Напиши /deals чтобы увидеть дешевые предложения.")

@dp.message_handler(commands=["deals"])
async def deals_cmd(msg: types.Message):
    df = parse_manomano("bosch")
    if df.empty:
        await msg.answer("Нет доступных предложений.")
    else:
        for _, row in df.iterrows():
            await msg.answer(f"{row['Название']}
Цена: {row['Цена']}
{row['Ссылка']}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    executor.start_polling(dp)
