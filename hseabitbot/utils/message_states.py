from aiogram.dispatcher.filters.state import State, StatesGroup


class MessageStates(StatesGroup):
    AskProgramAdd = State()
    AskProgramDel = State()
    AskUserId = State()
