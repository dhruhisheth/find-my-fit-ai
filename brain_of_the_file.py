# Setup GROQ API key 
import os 
GROQ_API_KEY = os.environ.get("GROQ_API_KEY") 

# Convert image to required format 
import base64

def encode_image(image_path):
    #image_path="fmf1.jpg"
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


# Setup Multimodal LLM
from groq import Groq
query = "Is this outfit combination going well together?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    Client = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    chat_completion = Client.chat.completions.create(
        messages = messages,
        model = model
    )

    return chat_completion.choices[0].message.content
