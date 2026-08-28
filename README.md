# AI Content-Summarizer & Study Tool

An intelligent web application that instantly converts URLs, from YouTube videos, articles, and GitHub READMEs, into actionable study materials powered by the Google GenAI SDK, FastAPI, and Streamlit. It delivers a concise summary that distills dense documentation or hours of video into a quick high-level overview, extracts deep key insights that surface architectural patterns and core principles, and formats everything into structured study notes for active recall and revision.

## Demo

coming soon...

## Features

1. Multi-Format Content Parsing: Automatically pulls clean text from YouTube videos, web articles, and documentation pages
2. Structured AI Summarization: Leverages the Gemini API and prompt engineering to break text down into a concise Summary, Key Concepts, and Active Recall Flashcards (with Questions and Answers)
3. FastAPI Backend: A robust asynchronous API handling parsing requests and communicating with Google's generative AI models
4. Streamlit Frontend: An interactive, clean user interface designed for quick studying and note generation
  
## Project Structure

```
content_summarizer/
│
├── backend.py       # FastAPI server and Gemini integration
├── app.py           # Streamlit user interface
├── parsers.py       # URL content extraction utilities
├── requirements.txt # Project dependencies
└── .env             # Environment configuration (API keys)
```
## Architecture

```
User inputs a URL in Streamlit Frontend
  ↓
Streamlit (app.py) sends a POST request with the URL to FastAPI backend
  ↓
FastAPI backend receives the request and calls the content extraction pipeline (parsers.py)
  ↓
Parsers extract raw text/transcripts based on source type (YouTube transcripts, Articles via BeautifulSoup, or GitHub READMEs)
  ↓
Google GenAI SDK (Gemini API) processes the extracted text to synthesize the summary, key insights, and structured study notes / flashcards
  ↓
FastAPI backend returns the formatted markdown notes as a JSON response
  ↓
Streamlit renders the generated output and success message in the browser
```

## Setup & Initialization

1. Clone the Repository and Navigate to Directory
git clone <repository-url>
cd content_summarizer

2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate
