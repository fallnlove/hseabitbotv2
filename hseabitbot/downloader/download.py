import requests
import pandas
import numpy

from ..parser import parse
from ..bot import mailing

bachelor_programs = [
    'BD_Akter',
    'BD_Ant_Ist',
    'BD_Ant_Fil',
    'BD_Bible',
    'BD_BI',
    'BD_Vostok',
    'BD_GGIGT',
    'BD_ZHur',
    'BD_InYaz',
    'BD_ITSS',
    'BD_IVT',
    'BD_IB',
    'BD_ISTR',
    'BD_Isk',
    'BD_Film',
    'BD_CMB',
    'BD_KogNeir',
    'BD_Compds',
    'BD_Cultural',
    'BD_Marketing',
    'BD_Math',
    'BD_Media',
    'BD_ir',
    'BD_icef',
    'BD_MO',
    'BD_MB',
    'BD_WE',
    'BD_Moda',
    'BD_Political',
    'BD_Pravo',
    'BD_AM',
    'BD_AMI',
    'BD_Data',
    'BD_epa',
    'BD_SE',
    'BD_Psy',
    'BD_AD',
    'BD_CPM',
    'BD_Art',
    'BD_Soc',
    'BD_Producer',
    'BD_bba',
    'BD_Creative',
    'BD_Logistics',
    'BD_Physics',
    'BD_Philology',
    'BD_Phil',
    'BD_Ling',
    'BD_Chem',
    'BD_dlawyer',
    'BD_digital',
    'BD_Stat',
    'BD_EA',
    'BD_Iran',
    'BD_India'
]

file_hashes = dict()


async def download_file(url: str) -> numpy.ndarray:
    file = requests.get(url)
    pandas_transformed_file = pandas.read_excel(file.content, 'TDSheet')
    return pandas_transformed_file.to_numpy()


async def hash_file(table: numpy.ndarray) -> int:
    return table[8, 2]


async def main() -> None:
    for program in bachelor_programs:
        url = f"https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/{program}.xlsx"
        table = await download_file(url)
        if hash_file(table) == file_hashes[program]:
            continue
        file_hashes[program] = hash_file(table)
        text = await parse.main(table)
        await mailing.main(program, text)
