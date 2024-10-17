from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from core.settings import settings
from services.players_manager import PlayerManager
from services.rcon import MinecraftRcon
from telegram_bot.keyboards import cancel as cancel_keyboard
from telegram_bot.keyboards import main

from .start import start

router = Router()
manager = PlayerManager()
minecraft_rcon = MinecraftRcon(
    settings.minecraft_server.ip,
    settings.minecraft_server.rcon_port,
    settings.minecraft_server.rcon_password,
)


class ChangeNick(StatesGroup):
    new_nick = State()


@router.callback_query(F.data == "health")
async def health(callback: CallbackQuery) -> None:
    nick = await manager.get_player_nick(callback.from_user.id)
    await minecraft_rcon.health(nick)
    await callback.answer()


@router.callback_query(F.data == "hunger")
async def hunger(callback: CallbackQuery) -> None:
    nick = await manager.get_player_nick(callback.from_user.id)
    await minecraft_rcon.hunger(nick)
    await callback.answer()


@router.callback_query(F.data == "day")
async def day(callback: CallbackQuery) -> None:
    await minecraft_rcon.day()
    await callback.answer()


@router.callback_query(F.data == "night")
async def night(callback: CallbackQuery) -> None:
    await minecraft_rcon.night()
    await callback.answer()


@router.callback_query(F.data == "tp")
async def tp(callback: CallbackQuery) -> None:
    await callback.answer()


@router.callback_query(F.data == "change_nick")
async def change_nick_first_step(
    callback: CallbackQuery, bot: Bot, state: FSMContext
) -> None:
    await state.set_state(ChangeNick.new_nick)
    await bot.edit_message_text(
        "Хорошо, введи свой новый ник🙄",
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=cancel_keyboard,
    )


@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery, bot: Bot, state: FSMContext) -> None:
    await state.clear()
    player_nick = await manager.get_player_nick(callback.from_user.id)
    await bot.edit_message_text(
        f"Привет, {player_nick}🙃",
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=main,
    )


@router.message(ChangeNick.new_nick)
async def change_nick_final_step(message: Message, state: FSMContext) -> None:
    result = await manager.change_player_nick(message.from_user.id, message.text)
    await state.clear()
    if result:
        await start(message, state)
    else:
        await message.answer("К сожалению этот ник уже занят🥹", reply_markup=main)
