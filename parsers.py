import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

def extract_content(url: str) -> str:
    try:
        if "youtube.com" in url or "youtu.be" in url:
            if "v=" in url:
                video_id = url.split("v=")[1].split("&")[0]
            else:
                video_id = url.split("/")[-1]
            
            yt_api = YouTubeTranscriptApi()
            transcript_list = yt_api.fetch(video_id)

            return " ".join(item.text for item in transcript_list)
        
        elif "github.com" in url and "blob" in url:
            raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            response = requests.get(raw_url)
            return response.text
        
        else:
            # uses the "User-Agent" header to trick the server into thinking the request is coming from a standard web browser, ensuring that the site actually responds
            headers = {"User-Agent": "Modzilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            return " ".join([p.get_text() for p in paragraphs])
        
    except Exception as e:
        raise ValueError(f"Could not extract text from URL: {e}")

        
        
