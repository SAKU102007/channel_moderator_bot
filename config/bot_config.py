from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = dotenv_values("./config/.env")
API_TOKEN = config["API_TOKEN"]
ADMIN = config["ADMIN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
