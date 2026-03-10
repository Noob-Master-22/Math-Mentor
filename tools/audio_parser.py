import groq
import os
from dotenv import load_dotenv

load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_math_from_audio(audio_bytes: bytes, filename: str = "audio.m4a") -> tuple[str, bool]:  
    try:
        transcription = client.audio.transcriptions.create(
            file=(filename, audio_bytes),  
            model="whisper-large-v3",
            response_format="verbose_json"
        )
        text = transcription.text.strip()
        low_confidence = len(text) < 10
        return text, low_confidence

    except Exception as e:
        return f"Audio transcription failed: {str(e)}", True
