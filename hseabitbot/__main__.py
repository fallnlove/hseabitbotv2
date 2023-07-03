import asyncio
import aiogram
from __init__ import __init__
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from downloader import download
from hseabitbot.utils import errors
from commands import start


async def main() -> None:
    hseabitbot = aiogram.Bot(token='5449720417:AAFPCL6HxUEG6IYYT1dpS_eRbxuM9Y5Z-T4')
    try:
        disp = aiogram.Dispatcher(bot=hseabitbot)
        disp.register_message_handler(start.start_handler)
        schedule = AsyncIOScheduler()
        schedule.add_job(download.main, 'cron', minute=f'5-59/5')
        schedule.start()
        await disp.start_polling()
    except Exception as error:
        print(error)

__init__()
asyncio.run(main())
