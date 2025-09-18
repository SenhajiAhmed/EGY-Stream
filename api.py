import requests
import json
import urllib.parse

def search_videos():
    # 1. Get user input
    query = input("Enter your search query: ").strip()
    
    # 2. Encode the query for the URL
    encoded_query = urllib.parse.quote(query)
    
    # 3. Build the API URL
    api_url = (
        f"https://ma3ak.top/api/v1/search/videos?"
        f"start=0&count=10&search={encoded_query}&sort=-match&searchTarget=local&nsfw=false&nsfwFlagsIncluded=0"
    )
    
    # 4. Send GET request
    response = requests.get(api_url)
    
    # 5. Check for successful response
    if response.status_code == 200:
        data = response.json()
        
        # 6. Save JSON to file
        filename = f"search_results.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Search results saved to {filename}")
    else:
        print(f"Failed to fetch results. Status code: {response.status_code}")

if __name__ == "__main__":
    search_videos()
