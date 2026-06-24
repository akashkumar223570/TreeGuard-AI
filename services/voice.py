
import edge_tts
import asyncio
import uuid

def generate_voice(text):

    filename = f"audio_{uuid.uuid4()}.mp3"

    async def _speak():
        communicate = edge_tts.Communicate(
            text,
            voice="en-IN-NeerjaNeural"

        )
        await communicate.save(filename)

    asyncio.run(_speak())

    return filename