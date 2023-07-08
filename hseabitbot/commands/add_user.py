import asyncio
import aiogram
import sqlite3

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from utils import message_states
from db_commands import add_info


async def get_program_name(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.finish()
    program_name = event.text
    user_id = event.from_id
    try:
        await add_info.add_user_sending(program_name, user_id)
        await event.reply('Успешно добавлено!')
    except sqlite3.OperationalError:
        await event.reply('Такой программы нет')
    except sqlite3.IntegrityError:
        await event.reply('Ты уже подписался на эту рассылку')


async def add_user(event: aiogram.types.Message, state: FSMContext) -> None:
    await event.answer(f"""Отправьте название программы с помощью inline бота
Введите @hseabitbot и название вашей программы, после чего выберите ее в списке""")
    await state.set_state(message_states.MessageStates.AskProgramAdd)
