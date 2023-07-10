import aiogram


inline_button = aiogram.types.InlineKeyboardButton(
    text='Введите название программы',
    switch_inline_query_current_chat=''
)

keyboard = aiogram.types.InlineKeyboardMarkup().add(inline_button)
