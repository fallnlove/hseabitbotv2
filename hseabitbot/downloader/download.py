import aiogram
import aiohttp
import pandas
import numpy

from parser import parse
from bot import mailing
from utils import config

bachelor_programs = config.bachelor_programs

file_hashes = {
}


async def download_file(url: str) -> numpy.ndarray:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as file_content:
            file = await file_content.read()
            pandas_transformed_file = pandas.read_excel(file, 'TDSheet')
            return pandas_transformed_file.to_numpy()


async def hash_file(table: numpy.ndarray) -> int:
    return table[8, 2]


async def main(bot: aiogram.Bot) -> None:
    for program in bachelor_programs:
        url = f"https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/{program}.xlsx"
        table = await download_file(url)
        if await hash_file(table) == file_hashes[program]:
            continue
        file_hashes[program] = await hash_file(table)
        text = await parse.main(table)
        await mailing.main(program, text, bot, table)
