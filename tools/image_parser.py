import os
import base64
from dotenv import load_dotenv
from groq import Groq
from PIL import Image
import io

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_math_from_image(image_bytes: bytes, mime_type: str = "image/jpeg") -> tuple[str, bool]:
    """
    Extract math problem from image using Groq's vision model (llama-4-scout).
    Returns: (extracted_text, low_confidence)
    """
    # Convert to JPEG if needed and compress to reduce token usage
    try:
        img = Image.open(io.BytesIO(image_bytes))
        if img.mode != "RGB":
            img = img.convert("RGB")
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=85)
        image_bytes = buffer.getvalue()
    except Exception:
        pass  # use original if conversion fails

    # Encode to base64 for API
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """You are a math problem extractor. Look at this image and extract the math problem.

Rules:
- Return ONLY the math problem text, nothing else
- Clean up formatting issues  
- Convert symbols to readable text (write 'sqrt(x)' not '√x', 'alpha' not 'α')
- If you cannot read the image clearly, start your response with 'UNCLEAR:'
- If there is no math problem visible, start with 'UNCLEAR:'

Extract the problem now:"""

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }],
            max_tokens=500
        )

        extracted = response.choices[0].message.content.strip()
        low_confidence = extracted.upper().startswith("UNCLEAR:")

        if low_confidence:
            extracted = extracted[8:].strip()

        return extracted, low_confidence

    except Exception as e:
        return f"Could not extract text from image: {str(e)}", True
