from rcon.source import rcon


class MinecraftRcon:
    def __init__(
        self, minecraft_server_ip: str, rcon_port: int, rcon_password: str
    ) -> None:
        self.minecraft_server_ip = minecraft_server_ip
        self.rcon_port = rcon_port
        self.rcon_password = rcon_password

    async def _request(self, command: str, *args: str) -> str:
        result = await rcon(
            command,
            *args,
            host=self.minecraft_server_ip,
            port=self.rcon_port,
            passwd=self.rcon_password,
        )
        return result

    async def health(self, player_nick: str) -> None:
        await self._request(
            "effect",
            "give",
            player_nick,
            "minecraft:instant_health",
            "1",
            "255",
        )
        await self._request(
            "effect",
            "give",
            player_nick,
            "minecraft:regeneration",
            "10",
            "2",
        )

    async def hunger(self, player_nick: str) -> None:
        await self._request(
            "effect",
            "give",
            player_nick,
            "minecraft:saturation",
            "1",
            "255",
        )

    async def tp_coordinates(self, player_nick: str, x: str, y: str, z: str) -> None:
        await self._request(
            "tp",
            player_nick,
            x,
            y,
            z,
        )

    async def tp_to_player(
        self, first_player_nick: str, second_player_nick: str
    ) -> None:
        await self._request(
            "tp",
            first_player_nick,
            second_player_nick,
        )

    async def day(self) -> None:
        await self._request("time", "set", "day")

    async def night(self) -> None:
        await self._request("time", "set", "night")
