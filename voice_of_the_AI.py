# Setup Text to Speech-TTS-model with gTTS
import os 
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )

    audioobj.save(output_filepath)

#input_text="Hi, This is FindMyFit AI"
#text_to_speech_with_gtts_old(input_text, output_filepath="fmf.mp3")


# Setup Text to Speech-TTS-model with ElevenLabs
import elevenlabs 
from elevenlabs.client import ElevenLabs 

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text,output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="PawMsb9h2MWDsRgzCXzT",
        model_id="eleven_turbo_v2"
    )
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")    


# Use model for text output to voice 
import subprocess 
import platform 

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )

    audioobj.save(output_filepath)
    os_name=platform.system()

    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'Start-Process -FilePath "{output_filepath}" -Wait']) 
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])    
        else:
            raise OSError("Unsupported Operating System")  
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}") 

#input_text = "This is FMF AI with autoplay."
#text_to_speech_with_gtts(input_text, output_filepath="fmf_gtts.mp3")


def text_to_speech_with_elevenlabs(input_text,output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="PawMsb9h2MWDsRgzCXzT",
        model_id="eleven_turbo_v2",
    )

    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    
    os_name=platform.system()

    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'Start-Process -FilePath "{output_filepath}" -Wait'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])    
        else:
            raise OSError("Unsupported Operating System")  
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}") 
    
#text_to_speech_with_elevenlabs(input_text, output_filepath="fmf_elevenlabs.mp3")    
