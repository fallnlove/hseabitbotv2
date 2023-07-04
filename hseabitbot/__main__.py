import asyncio
import aiogram
from __init__ import __init__
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from downloader import download
from utils import config
from bot import load_handlers


async def main() -> None:
    hseabitbot = aiogram.Bot(token=config.token)
    try:
        disp = aiogram.Dispatcher(bot=hseabitbot)
        await load_handlers.main(disp)

        schedule = AsyncIOScheduler()
        schedule.add_job(download.main, 'cron', minute=f'5-59/5')
        schedule.start()

        await disp.start_polling()
    except Exception as error:
        await hseabitbot.close_bot()
        print(error)

if __name__ == '__main__':
    __init__()
    asyncio.run(main())
