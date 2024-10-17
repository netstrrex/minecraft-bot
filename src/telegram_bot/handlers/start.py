from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from services.players_manager import PlayerManager
from telegram_bot.keyboards import main

router = Router()
manager = PlayerManager()


class Registration(StatesGroup):
    nick = State()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    if await manager.is_player_exist(message.from_user.id):
        player_nick = await manager.get_player_nick(message.from_user.id)
        await message.answer(f"Привет, {player_nick}🙃", reply_markup=main)
    else:
        await state.set_state(Registration.nick)
        await message.answer("Для использования бота введи свой ник😉")


@router.message(Registration.nick)
async def registration(message: Message, state: FSMContext) -> None:
    await manager.add_player(message.from_user.id, message.text)
    await state.clear()
    await start(message, state)
