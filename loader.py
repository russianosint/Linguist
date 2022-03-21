from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.config import BOT_TOKEN
from utils.db.storage import DBManager

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage) 
db = DBManager(directory='db.sqlite3')
