import asyncio
import aiogram
import sqlite3

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from utils import message_states
from db_commands import del_info


async def get_program_name(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.finish()
    program_name = event.text
    user_id = event.from_id
    try:
        await del_info.delete_user_sending(program_name, user_id)
        await event.reply('Убрал тебя из списка')
    except:
        await event.reply('Такой программы нет или ты уже отписался')


async def delete_user(event: aiogram.types.Message, state: FSMContext) -> None:
    await event.answer(f"""Отправьте название программы с помощью inline бота
Введите @hseabitbot и название вашей программы, после чего выберите ее в списке""")
    await state.set_state(message_states.MessageStates.AskProgramDel)
