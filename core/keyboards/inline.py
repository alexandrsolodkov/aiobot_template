from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

user_answer = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Купить рекламу в канале',
            callback_data='buy_advertising'
        )
    ],
    [
        InlineKeyboardButton(
            text='Прислать вакансию',
            callback_data='offer_vacancy'
        )
    ],
    [
        InlineKeyboardButton(
            text='Задать вопрос админам',
            callback_data='question'
        )
    ],
    [
        InlineKeyboardButton(
            text='Предложить пост в канал',
            callback_data='offer_news'
        )
    ]
])
