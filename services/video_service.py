import requests
from config import API_BASE_URL, VIDEO_DATA_FILE
from utils.file_manager import FileManager

class VideoService:
    def __init__(self, logger):
        self.logger = logger

    def fetch_video_data(self, video_id):
        url = f"{API_BASE_URL}/videos/{video_id}"
        self.logger.info(f"Fetching video data for ID {video_id}")
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            FileManager.save_json(VIDEO_DATA_FILE, data)
            self.logger.info("Video data saved")
            return data
        else:
            self.logger.error(f"Failed to fetch video data: {response.status_code}")
            return None
