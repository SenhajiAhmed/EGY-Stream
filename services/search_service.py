import requests
import urllib.parse
from config import API_BASE_URL, SEARCH_RESULTS_FILE
from utils.file_manager import FileManager
from models.video import Video

class SearchService:
    def __init__(self, logger):
        self.logger = logger

    def search_videos(self, query):
        encoded_query = urllib.parse.quote(query)
        url = f"{API_BASE_URL}/search/videos?start=0&count=10&search={encoded_query}&sort=-match&searchTarget=local&nsfw=false&nsfwFlagsIncluded=0"

        self.logger.info(f"Searching videos with query: {query}")
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            FileManager.save_json(SEARCH_RESULTS_FILE, data)
            self.logger.info(f"Results saved to {SEARCH_RESULTS_FILE}")
            return [Video(v["name"], v["shortUUID"], v.get("url")) for v in data.get("data", [])]
        else:
            self.logger.error(f"Failed with status {response.status_code}")
            return []
