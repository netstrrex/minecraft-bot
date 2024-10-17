from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Отмена", callback_data="cancel")]]
)
