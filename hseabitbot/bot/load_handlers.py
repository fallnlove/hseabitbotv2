import aiogram

from commands import start, add_user, set_user_id, delete_user
from utils import message_states
from inline_commands import inline_mode


async def main(disp: aiogram.Dispatcher) -> None:
    disp.register_message_handler(start.start_handler, commands={"start", "restart", "help"})
    disp.register_message_handler(add_user.add_user, commands={"add"})
    disp.register_message_handler(delete_user.delete_user, commands={"del"})
    disp.register_message_handler(set_user_id.set_user_id, commands={"set"})

    disp.register_message_handler(add_user.get_program_name, state=message_states.MessageStates.AskProgramAdd)
    disp.register_message_handler(delete_user.get_program_name, state=message_states.MessageStates.AskProgramDel)
    disp.register_message_handler(set_user_id.get_id, state=message_states.MessageStates.AskUserId)

    disp.register_inline_handler(inline_mode.answer_inline_query)
