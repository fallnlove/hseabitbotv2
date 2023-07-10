import asyncio
import aiogram

from ..utils import config


async def answer_inline_query(inline_query: aiogram.types.InlineQuery) -> None:
    text = inline_query.query.lower()
    results = []
    event_id = int(inline_query.id)
    counter = 0
    for program_name in config.program_names:
        if text in program_name.lower():
            counter += 1
            results.append(aiogram.types.InlineQueryResultArticle(
                id=str(event_id + counter),
                title=program_name,
                input_message_content=aiogram.types.InputTextMessageContent(
                    message_text=program_name,
                    parse_mode="HTML"
                )
            ))
        if counter >= 10:
            break
    await inline_query.answer(results, is_personal=True)
