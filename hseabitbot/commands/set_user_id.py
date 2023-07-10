import aiogram
import asyncio
import sqlite3

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from ..utils import message_states
from ..db_commands import add_info


async def get_id(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.finish()
    user_state_id = event.text
    user_id = event.from_id
    try:
        await add_info.add_user_id(user_id, user_state_id)
        await event.reply('Успешно добавлено!')
    except sqlite3.OperationalError:
        await add_info.change_user_id(user_id, user_state_id)
        await event.reply('Успешно изменено!')
    except sqlite3.IntegrityError:
        await add_info.change_user_id(user_id, user_state_id)
        await event.reply('Успешно изменено!')


async def set_user_id(event: aiogram.types.Message, state: FSMContext) -> None:
    await event.answer(f"""Отправьте свой номер СНИЛС в формате XXX-XXX-XXX XX""")
    await state.set_state(message_states.MessageStates.AskUserId)
