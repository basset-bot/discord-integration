from services.discord.actions.base import Base
import services.discord.support.fetch as fetch

class SendMessageToChannel(Base):
    @classmethod
    async def action(cls, message, channel_id):
        result = {}
        result['message'] = message

        channel = await fetch.text_channel(channel_id, result)
        if not channel: return result

        await channel.send(message)

        result['type'] = 'success'

        return result