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
        Analyze the following text and return clean Markdown with these exact sections. The titles of each section must have their own lines and be bigger than the rest:
        1. **Summary** (3-4 sentences overview)
        2. **Key Concepts and Insights** (Bullet points of deep takeaways)
        3. **Active Recall Flashcards** (3-5 Question & Answer pairs. Answers should be in a new line)

        Text to analyze:
        {raw_text[:12000]}
        '''

        response = client.models.generate_content(
            model = 'gemini-3.6-flash',
            contents = prompt,
        )

        return {"notes" : response.text}
    
    except Exception as e:
        print(f"Debug Error: {e}")
        raise HTTPException(status_code = 400, detail = str(e))

