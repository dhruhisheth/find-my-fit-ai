# Setup Audio recorder (ffmpeg & portaudio & pyaudio)
import logging 
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout = 20, phrase_time_limit = None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a user to start speaking in seconds.
    phrase_time_limit (int): Maximum time for the phrase to be recorded in seconds. 

    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            logging.info("Start speaking now")

            # Record audio
            audio_data = recognizer.listen(source, timeout = timeout, phrase_time_limit = phrase_time_limit)
            logging.info("Recording complete")

            # Convert the audio into MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format = "mp3", bitrate = "128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occured: {e}")

#audio_filepath = "dhruhi's voice.mp3"
#record_audio(file_path=audio_filepath)


# Setup Speech to text-SST-model for transcription
import os 
from groq import Groq 

GROQ_API_KEY= os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY ):
    Client= Groq(api_key=GROQ_API_KEY)
    audio_file=open(audio_filepath, "rb")
    transcription=Client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return transcription.text
