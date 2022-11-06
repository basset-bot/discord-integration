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
    async def execute(cls, *args, **kwargs):
        result = asyncio.run_coroutine_threadsafe(
            cls.action(*args, **kwargs),
            cls.discord.loop
        )
        
        return result.result()