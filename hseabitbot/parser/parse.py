import asyncio
import numpy
import numpy as np


async def replace_with_ones(table: numpy.ndarray) -> None:
    table[(table == 'Да') | (table == 'Yes')] = 1
    table[(table == 'Нет') | (table == 'No')] = 0


async def find_cell_with(table: numpy.ndarray, value: [int, str]) -> [int, int]:
    return numpy.argwhere(table == value)[0]


async def main(table: numpy.ndarray) -> str:
    await replace_with_ones(table)
    return f"""*{table[0, 2]}*
    {table[8, 2]}
    Бюджетных мест: *{table[5, 10]}*
    Квазибюджетных мест: *{table[6, 10]}*
    Подано заявлений БВИ: *{numpy.sum(table[16:, 4])}* (подали согласие: *{numpy.sum(table[16:, 4] *
                                                        table[16:, find_cell_with(table, 'Оригинал аттестата')[1]])}*)
    Подано заявлений по особой квоте: *{numpy.sum(table[16:, 6])}*
    Подано заявлений по целевой квоте: *{numpy.sum(table[16:, 8])}*
    Подано заявлений по специальной квоте: *{numpy.sum(table[16:, 10])}*
    """
