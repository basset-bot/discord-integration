import asyncio
import services.discord.client as client
import services.discord.support.fetch as fetch
from services.discord.support.id_name_builder import id_name_builder

class Base:
    discord = client.get()

    @classmethod
    async def action(cls):
        pass

    @classmethod
    async def discord_coroutine(cls, async_function, result=False):
        if not result:
            asyncio.run_coroutine_threadsafe(
                async_function,
                cls.discord.loop
            )
            return
            
        result = asyncio.run_coroutine_threadsafe(
            async_function,
            cls.discord.loop
        )
        
        return result.result()

    @classmethod
    async def execute(cls, *args, **kwargs):
        return await cls.discord_coroutine(cls.action(*args, **kwargs), result=True)