import asyncio
import aiogram

from db_commands import get_info


async def main(program_name: str, msg_text: str, bot: aiogram.Bot) -> None:
    user_list = await get_info.get_user_list(program_name)
    for user_id in user_list:
        try:
            await bot.send_message(chat_id=user_id[0], text=msg_text, parse_mode=aiogram.types.ParseMode.MARKDOWN)
        except:
            pass
