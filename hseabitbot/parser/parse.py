import asyncio
import numpy


async def replace_with_ones(table: numpy.ndarray) -> None:
    table[(table == 'Да') | (table == 'Yes')] = 1
    table[(table == 'Нет') | (table == 'No')] = 0


async def main(table: numpy.ndarray) -> str:
    await replace_with_ones(table)
    return f"""*{table[0, 2]}*
    {table[8, 2]}
    Бюджетных мест: *{table[5, 10]}*
    Квазибюджетных мест: *{table[6, 10]}*
    Подано заявлений БВИ: *{numpy.sum(table[16:, 4])}* (подали согласие: *{counter_sogl_bvi}*)
    Подано заявлений по особой квоте(не более {info[4]}): *{numpy.sum(table[16:, 6])}*
    Подано заявлений по целевой квоте(не более {info[5]}): *{numpy.sum(table[16:, 8])}*
    Подано заявлений по специальной квоте(не более {info[6]}): *{numpy.sum(table[16:, 10])}*
    """
