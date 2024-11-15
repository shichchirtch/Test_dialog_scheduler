from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import StorageKey, MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

aio_storage = MemoryStorage()

class FSM_ST(StatesGroup):
    start = State()  # FSM_ST:start



BOT_TOKEN =    '<BOT_TOKEN>'

bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

bot_storage_key = StorageKey(bot_id=bot.id, user_id=bot.id, chat_id=bot.id)

dp = Dispatcher(storage=aio_storage)
