from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv
from parsers import extract_content

load_dotenv()
app = FastAPI(title="AI Content Summarizer API")

# initialize Gemini client securely
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

class SummarizeRequest(BaseModel):
    url: str

@app.post("/api/summarize")
def summarize_content(request: SummarizeRequest):
    try:
        raw_text = extract_content(request.url)

        prompt = f'''
        Analyze the following text and return clean Markdown with these exact sections:
        1. Executive Summary (3-4 sentences overview)
        2. Key Concepts and Insights (Bullet points of deep takeaways)
        3. Active Recall Flashcards (3-5 Question & Answer pairs)

        Text to analyze:
        {raw_text[:12000]}
        '''

        response = client.models.generate_content(
            model = 'gemini_2.5-flash',
            contents = prompt,
        )

        return {"notes" : response.txt}
    
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

