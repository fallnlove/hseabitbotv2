import asyncio
import aiogram
from hseabitbot import __init__
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from hseabitbot.downloader import download
from hseabitbot.utils import config
from hseabitbot.bot import load_handlers


async def main() -> None:
    hseabitbot = aiogram.Bot(token=config.token)
    try:
        storage = MemoryStorage()
        disp = aiogram.Dispatcher(bot=hseabitbot, storage=storage)
        await load_handlers.main(disp)

        schedule = AsyncIOScheduler()
        schedule.add_job(download.main, 'cron', minute=f'0-59/10', args=[hseabitbot])
        schedule.start()

        await disp.start_polling()
    except Exception as error:
        await hseabitbot.close_bot()
        print(error)

if __name__ == '__main__':
    __init__()
    asyncio.run(main())
