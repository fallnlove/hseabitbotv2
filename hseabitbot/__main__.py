import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from downloader import download
from hseabitbot.utils import errors


async def main() -> None:
    try:
        schedule = AsyncIOScheduler()
        schedule.add_job(download.main, 'cron', minute=f'0-59/5')
        schedule.start()
        asyncio.get_event_loop().run_forever()
    except Exception as error:
        pass  # do something
