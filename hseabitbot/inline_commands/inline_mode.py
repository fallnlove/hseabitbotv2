import asyncio
import aiogram

from utils import config


async def answer_inline_query(inline_query: aiogram.types.InlineQuery) -> None:
    text = inline_query.query.lower()
    results = []
    event_id = int(inline_query.id)
    counter = 0
    for program_id, program_name in zip(config.bachelor_programs, config.program_names):
        if text in program_name.lower():
            counter += 1
            results.append(aiogram.types.InlineQueryResultArticle(
                id=str(event_id + counter),
                title=program_name,
                input_message_content=aiogram.types.InputTextMessageContent(
                    message_text=program_id,
                    parse_mode="HTML"
                )
            ))
        if counter >= 10:
            break
    await inline_query.answer(results[:20], is_personal=True)
