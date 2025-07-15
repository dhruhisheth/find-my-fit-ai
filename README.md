# FindMyFit.AI

A high‑end personal stylist voice assistant built with Gradio, Groq multimodal LLM, and ElevenLabs (with a gTTS fallback). Upload or record your outfit photo and voice prompt, and receive professional styling advice spoken back to you.

---

## Features

* **Voice Input:** Record live via microphone or upload an audio file for transcription (via Groq’s `whisper-large-v3`).
* **Image Analysis:** Submit an outfit photo; the multimodal Groq model analyzes color harmony, fit, and styling.
* **Voice Output:** AI‑generated styling advice is spoken back using ElevenLabs TTS (fallback to gTTS).
* **Deployable:** Run locally with Python & Gradio, or deploy on Render, Hugging Face Spaces, Docker, etc.

---

## 🧰 Tech Stack & Requirements

* **Python ≥3.9**
* **Gradio** for the web UI
* **groq** SDK for audio transcription & multimodal chat
* **elevenlabs** Python client (paid/free tier with limitations)
* **gTTS** as a free fallback for TTS
* **requests**, **Pillow**, **pydub**, **speech\_recognition**

### Environment Variables

Create a `.env` file (or set in your shell/hosting platform):

```bash
GROQ_API_KEY=<your Groq API key>
ELEVENLABS_API_KEY=<your ElevenLabs API key>
```

> **Note:** ElevenLabs free tier is limited and may be disabled for unusual activity. Consider a paid plan or fallback to gTTS.

---

## 🚀 Installation & Local Run

### 1. Clone the repo:

   ```bash
git clone [https://github.com/yourusername/find-my-fit-ai.git](https://github.com/yourusername/find-my-fit-ai.git)
cd find-my-fit-ai

   ```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
````

### 3. Set environment variables:

```bash
export GROQ\_API\_KEY=...
export ELEVENLABS\_API\_KEY=...
```


### 4. Launch the Gradio app:
   ```bash
python app.py
````

#### 5. Open your browser at `http://localhost:8080`.

---

## ☁️ Deployment

### Render.com

* Add a **Web Service** pointing to this GitHub repo.
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `python app.py`
* **Port:** `8080`
* Set environment vars in Dashboard under **Settings > Environment**.

### Hugging Face Spaces

* Create a new **Gradio Space** and point its Git to this repo.
* Ensure `requirements.txt` and `app.py` are present.
* Under **Settings**, add your API keys as Secrets.

---

## ⚖️ License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
