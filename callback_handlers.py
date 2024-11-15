import asyncio
from aiogram import Router
from aiogram.types import CallbackQuery
from bot_instance import dp, bot_storage_key
from aiogram.fsm.context import FSMContext
from external_functions import scheduler_job

cb_router = Router()


@cb_router.callback_query()
async def command_start_process(cb:CallbackQuery, state:FSMContext):
    print('callback works')
    scheduler_job(cb)
