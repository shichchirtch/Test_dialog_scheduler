from aiogram import Router
import asyncio
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
# from filters import PRE_START, IS_ADMIN
from aiogram.fsm.context import FSMContext
from bot_instance import FSM_ST
from keyboards import first_inline_kb


ch_router = Router()


@ch_router.message(CommandStart())
async def command_start_process(message:Message, state:FSMContext):
    await state.set_data({'foto_id':'', 'lan':'ru'})
    await message.answer(text=f'👋\n\n<b>Привет, {message.from_user.first_name}!</b>\n'
           'Это планировщик бот. скажи мне когда произойдёт важное для тебя событие'
                              ' и я напомню тебе о нем забалаговременно !\n\nУдобно, не правда ли ?', reply_markup=first_inline_kb)