import asyncio
import aiogram
import sqlite3

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from ..utils import message_states, inline_keyboard
from ..db_commands import add_info


async def get_program_name(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.finish()
    program_name = event.text
    user_id = event.from_id
    try:
        await add_info.add_user_sending(program_name, user_id)
        await event.reply('Успешно добавлено!')
    except sqlite3.OperationalError:
        await event.reply('Такой программы нет')
    except KeyError:
        await event.reply('Такой программы нет')
    except sqlite3.IntegrityError:
        await event.reply('Ты уже подписался на эту рассылку')


async def add_user(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.set_state(message_states.MessageStates.AskProgramAdd)
    await event.answer(f"""Нажмите на кнопку снизу, введите название программы и выберите ее в списке

Если инлайн режим не работает, то просто скопируйте название программы с сайта [ВШЭ](https://ba.hse.ru/base2023) \
и отправьте боту""",
                       reply_markup=inline_keyboard.keyboard, parse_mode=aiogram.types.ParseMode.MARKDOWN,
                       disable_web_page_preview = True)
