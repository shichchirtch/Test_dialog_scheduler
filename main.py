import asyncio
from command_handlers import ch_router
from bot_instance import bot, bot_storage_key, dp, scheduler
from aiogram_dialog import setup_dialogs
from callback_handlers import cb_router


async def main():

    await dp.storage.set_data(key=bot_storage_key, data={})
    scheduler.start()
    dp.include_router(ch_router)
    dp.include_router(cb_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    setup_dialogs(dp)
    await dp.start_polling(bot)

asyncio.run(main())