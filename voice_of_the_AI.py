# voice_of_the_AI.py
import os
from gtts import gTTS
import subprocess, platform
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_gtts(input_text, output_filepath):
    audioobj = gTTS(text=input_text, lang="en", slow=False)
    audioobj.save(output_filepath)
    return output_filepath

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="PawMsb9h2MWDsRgzCXzT",
        model_id="eleven_turbo_v2"
    )
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    return output_filepath
