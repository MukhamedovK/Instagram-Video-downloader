import logging

from aiogram import Bot, Dispatcher, executor, types

from config import *
from utils import *


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Hello!\nTo get started use the command: \n/insta username")


@dp.message_handler(commands=['insta'])
async def insta_handler(message: types.Message):
    text = message.text.split(" ")
    if len(text) == 2:
        print(text[-1])
        await video_downloader(text[-1])
        videos = await scaner_folders()

        for video in videos:
            await message.answer_video(types.InputFile(video), caption=f"#{text[-1]}")
            await delete_folders()
    else:
        await message.answer("Please, use /insta username")


if __name__ == "__main__":
    executor.start_polling(dp)
