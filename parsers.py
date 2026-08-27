import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

def extract_content(url: str) -> str:
    try:
        if "youtube.com" in url:
            if "v=" in url:
                video_id = url.split("v=")[1].split("&")[0]
            else:
                video_id = url.split("/")[-1]
            
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            return " ".join(item['text'] for item in transcript_list)