from services.discord.actions.base import Base
import services.discord.support.fetch as fetch

class SendMessageToChannel(Base):
    @classmethod
    async def action(cls, message, channel_id):
        result = {}
        result['message'] = {
            'content': message
        }

        channel = await fetch.text_channel(channel_id, result)
        if not channel: return result

        sent_message = await channel.send(message)

        result['type'] = 'success'
        result['message']['id'] = sent_message.id

        return result