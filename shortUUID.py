import json

# Load JSON
with open("search_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

videos = data.get("data", [])

# Display videos with numbers
for idx, video in enumerate(videos, start=1):
    print(f"{idx}. {video['name']}")

# Get user choice
choice = int(input("\nEnter the number of the video you want: "))

if 1 <= choice <= len(videos):
    selected_video = videos[choice - 1]
    print(f"\nYou selected: {selected_video['name']}")
    print(f"ShortUUID: {selected_video['shortUUID']}")
else:
    print("Invalid choice.")
