import requests
import json

video_id = "fKrcVFy5UXSC8Nyc1PNycd"
api_url = f"https://ma3ak.top/api/v1/videos/{video_id}"

response = requests.get(api_url)
data = response.json()

# Save JSON to a local file
with open("video_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON saved as video_data.json")
