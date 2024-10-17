import asyncio
import json

import aiofiles

from core.settings import BASE_DIR


class PlayerManager:
    def __init__(self) -> None:
        self._file_lock = asyncio.Lock()
        self._file_path = BASE_DIR / "players.json"

    async def _read(self) -> dict:
        async with self._file_lock:
            async with aiofiles.open(self._file_path) as file:
                data = await file.read()
        return json.loads(data)

    async def _write(self, data: dict) -> None:
        async with self._file_lock:
            async with aiofiles.open(self._file_path, "w") as file:
                await file.write(json.dumps(data))

    async def is_player_exist(self, telegram_id: int) -> bool:
        data = await self._read()
        for player in data["players"]:
            if player["telegram_id"] == telegram_id:
                return True
        return False

    async def add_player(self, telegram_id: int, nick: str) -> None:
        data = await self._read()
        data["players"].append({"telegram_id": telegram_id, "nick": nick})
        await self._write(data)

    async def change_player_nick(self, telegram_id: int, new_nick: str) -> bool:
        data = await self._read()
        nicks = [player["nick"] for player in data["players"]]
        if new_nick in nicks:
            return False
        for player in data["players"]:
            if player["telegram_id"] == telegram_id:
                player["nick"] = new_nick
        await self._write(data)
        return True

    async def get_player_nick(self, telegram_id: int) -> str:
        data = await self._read()
        for player in data["players"]:
            if player["telegram_id"] == telegram_id:
                nick = player["nick"]

        return nick
