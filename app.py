# app.py
import os
import gradio as gr
from brain_of_the_file import encode_image, analyze_image_with_query
from voice_of_the_user import record_audio, transcribe_with_groq
from voice_of_the_AI import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """You are a high-end personal stylist... (unchanged)"""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    if image_filepath:
        FMF_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        FMF_response = "No image provided for me to analyze"

    # Try ElevenLabs, fallback to gTTS
    try:
        audio_path = text_to_speech_with_elevenlabs(
            input_text=FMF_response,
            output_filepath="final.mp3"
        )
    except Exception as e:
        print(f"ElevenLabs TTS failed ({e}), falling back to gTTS")
        audio_path = text_to_speech_with_gtts(
            input_text=FMF_response,
            output_filepath="final.mp3"
        )

    return speech_to_text_output, FMF_response, audio_path


gradio_interface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources="microphone", type="filepath"),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Fashion Expert's Response"),
        gr.Audio(type="filepath", label="AI Voice Response"),
    ],
    title="FindMyFit.AI"
)

gradio_interface.launch(server_name="0.0.0.0", server_port=8080)
