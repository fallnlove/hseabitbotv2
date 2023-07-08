import asyncio
import aiogram


async def answer_inline_query(inline_query: aiogram.types.InlineQuery) -> None:
    text = inline_query.query + '1'
    results = []
    results.append(aiogram.types.InlineQueryResultArticle(
        id=link,  # ссылки у нас уникальные, потому проблем не будет
        title=inline_query.query,
        description=link_data["description"],
        input_message_content=InputTextMessageContent(
            message_text=get_message_text(
                link=link,
                title=link_data["title"],
                description=link_data["description"]
            ),
            parse_mode="HTML"
        )
    ))
    await inline_query.answer(text, is_personal=True)
