
from aiogram.types import CallbackQuery
from datetime import datetime, timedelta
from bot_instance import bot, scheduler, FSM_ST
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
# from aiogram_dialog.manager import BackgroundDialogManager
# from aiogram_dialog.api.bg_manager import BackgroundDialogManager


async def mahnung_gearbeitet(bot, user_id):
    print('WE are into mahnung gearbeitet function')
    # print('nach bg_manager   ---> ', bg_manager)
    # bg_manager = DialogManager.bg(self=manager, user_id=user_id, chat_id=chat_id, stack_id=stack_id)
    await bot.send_message(chat_id=user_id, text="Mahnung !")
    # await bg_manager.done()#switch_to(state=FSM_ST.nach_mahnung_accepting)


def scheduler_job(callback: CallbackQuery):
    user_id = callback.from_user.id
    print(f'scheduler_job works for user {user_id}')
    time_now = datetime.now()  # Время сейчас
    print('time_now = ', time_now)
    delta = timedelta(seconds=10)  # Время, Через которое придёт сообщуха
    future = time_now+delta  # Время когда действие должно быть закончено
    stop_exam = 'exam'+str(user_id)
    print('8888888')
    scheduler.add_job(mahnung_gearbeitet, "date", run_date=future, args=(bot, user_id), id=stop_exam)
