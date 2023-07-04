import aiogram

from commands import start


async def main(disp: aiogram.Dispatcher) -> None:
    disp.register_message_handler(start.start_handler, commands={"start", "restart", "help"})
