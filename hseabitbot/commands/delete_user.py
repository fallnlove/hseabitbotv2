import asyncio
import aiogram
import sqlite3

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from ..utils import message_states, inline_keyboard
from ..db_commands import del_info


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
    await state.set_state(message_states.MessageStates.AskProgramDel)
    await event.answer(f"""Нажмите на кнопку снизу, введите название программы и выберите ее в списке

    Если инлайн режим не работает, то просто скопируйте название программы с сайта [ВШЭ](https://ba.hse.ru/base2023) \
    и отправьте боту""",
                       reply_markup=inline_keyboard.keyboard, parse_mode=aiogram.types.ParseMode.MARKDOWN,
                       disable_web_page_preview=True)
