from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Здоровье❤️", callback_data="health"),
            InlineKeyboardButton(text="Голод🍗", callback_data="hunger"),
        ],
        [
            InlineKeyboardButton(text="День☀️", callback_data="day"),
            InlineKeyboardButton(text="Ночь🌚", callback_data="night"),
        ],
        [
            InlineKeyboardButton(text="Телепортировать✨", callback_data="tp"),
        ],
        [InlineKeyboardButton(text="Изменить ник🔧", callback_data="change_nick")],
    ]
)
