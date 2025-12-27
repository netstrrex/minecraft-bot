from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def tp_players_keyboard(players: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for nick in players:
        builder.button(
            text=nick,
            callback_data=f"tp_to:{nick}",
        )

    builder.button(text="Отмена", callback_data="cancel")
    builder.adjust(2)

    return builder.as_markup()
