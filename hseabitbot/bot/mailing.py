import asyncio
import aiogram
import numpy

from db_commands import get_info
from parser import parse


async def get_position(user_id: int, table: numpy.ndarray) -> int:
    try:
        state_id = await get_info.get_user_state_id(user_id)
        row_num = (await parse.find_cell_with(table, state_id))[0]
        return int(table[row_num, 0])
    except:
        return -1


async def main(program_name: str, msg_text: str, bot: aiogram.Bot, table: numpy.ndarray) -> None:
    user_list = await get_info.get_user_list(program_name)
    for user_id in user_list:
        try:
            user_string = ""
            pos = await get_position(user_id[0], table)
            if pos > 0:
                user_string = f"\nМесто в списке: *{pos}*"
            await bot.send_message(chat_id=user_id[0], text=msg_text + user_string,
                                   parse_mode=aiogram.types.ParseMode.MARKDOWN)
        except:
            pass
