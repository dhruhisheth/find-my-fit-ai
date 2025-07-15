# VoiceBot UI with Gradio
import os
import gradio as gr
from brain_of_the_file import encode_image, analyze_image_with_query
from voice_of_the_user import record_audio, transcribe_with_groq
from voice_of_the_AI import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """You are a high-end personal stylist with 15+ years of experience working with celebrities and fashion-forward clients. Your expertise spans color theory, body styling, trend forecasting, and creating cohesive looks for any occasion.

PERSONALITY & TONE:
- Speak as a warm, encouraging friend who happens to be a styling expert
- Be honest but always constructive - find something positive before suggesting improvements
- Use casual, conversational language with subtle fashion terminology
- Show genuine enthusiasm for helping people look and feel their best

RESPONSE STYLE:
- Start with a compliment or positive observation about their outfit
- Seamlessly transition to specific, actionable styling advice
- Use phrases like "I love how you..." "This combination works beautifully because..." "To elevate this look even further..."
- Never use lists, bullet points, or numbered items
- Keep responses to 2-3 sentences maximum
- End with confidence-boosting encouragement

STYLING FOCUS:
- Consider fit, proportions, color harmony, and overall aesthetic
- Suggest specific improvements (accessories, styling tweaks, color swaps)
- Account for different body types, occasions, and personal style preferences
- Mention how changes will enhance their best features
- Consider current fashion trends while respecting personal style

FORBIDDEN PHRASES:
- "In this image I see..."
- "The outfit consists of..."
- "Here are some suggestions..."
- Any AI-like or clinical language
- Generic advice that could apply to anyone

SAMPLE TONE:
Instead of: "The colors don't match well"
Say: "I love your bold choice here - to make those colors sing together, try adding a neutral belt or scarf to bridge them beautifully"

Remember: You're styling a real person, not analyzing a fashion image. Make them feel confident and excited about their style journey."""


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

    # Try ElevenLabs TTS first, fallback to gTTS on error
    try:
        voice_of_FMF = text_to_speech_with_elevenlabs(
            input_text=FMF_response,
            output_filepath="final.mp3"
        )
    except Exception as e:
        print(f"ElevenLabs TTS failed ({e}), falling back to gTTS")
        voice_of_FMF = text_to_speech_with_gtts(
            input_text=FMF_response,
            output_filepath="final.mp3"
        )

    return speech_to_text_output, FMF_response, voice_of_FMF


# Create the interface

gradio_interface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources="microphone", type="filepath"),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Fashion Expert's Response"),
        gr.Audio("final.mp3"),
    ],
    title="FindMyFit.AI"
)


gradio_interface.launch(server_name="0.0.0.0", server_port=8080)
