import asyncio
import aiogram

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class MessageStates(StatesGroup):
    AskProgram = State()


async def get_program_name(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.reset_state()


async def add_user(event: aiogram.types.Message, state: FSMContext) -> None:
    await event.answer(f"""Отправьте название программы с помощью inline бота""")
    await state.set_state(MessageStates.AskProgram)
