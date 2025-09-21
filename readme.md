# 📺 Video Search & Streaming Project
This project allows you to **search videos**, fetch **metadata and playlists**, and play streams using **mpv**.  
It is refactored into a clean **Object-Oriented Python project** with multiple files and services.  

## 🚀 Features
- 🔍 Search for videos via `ma3ak.top` API  
- 📂 Save search results and video data to JSON files  
- 🎥 Extract **HLS master playlists** that combine audio & video  
- 📊 Display available resolutions (width, height, fps, size)  
- ▶️ Play video streams directly with **mpv**  

## ✅ Prerequisites
- Python 3.9+
- `mpv` media player installed and available on PATH
  - Ubuntu/Debian: `sudo apt-get install mpv`
  - Arch: `sudo pacman -S mpv`
  - macOS (Homebrew): `brew install mpv`

## 📂 Project Structure
```text
EGY-Stream/
├─ main.py
├─ config.py
├─ requirements.txt
├─ readme.md
├─ .gitignore
├─ services/
│  ├─ search_service.py
│  ├─ video_service.py
│  ├─ playlist_service.py
│  └─ player_service.py
├─ models/
│  ├─ video.py
│  └─ playlist.py
└─ utils/
   ├─ file_manager.py
   └─ logger.py
```

## ⚙️ Installation
1. Clone this repository and enter the project directory:
   ```bash
   git clone https://github.com/SenhajiAhmed/EGY-Stream.git
   cd EGY-Stream
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Configuration
Edit `config.py` to adjust defaults:
- `API_BASE_URL`: Base URL of the API (default: `https://ma3ak.top/api/v1`)
- `SEARCH_RESULTS_FILE`: Path to save search results (default: `search_results.json`)
- `VIDEO_DATA_FILE`: Path to save video metadata (default: `video_data.json`)

Root-level JSON files are ignored via `.gitignore`.

▶️ Usage

Run the main script:
```bash
python main.py
```

Steps:
- Enter your search query
- Choose a video from the list
- The app fetches video metadata and extracts the HLS master playlist
- A master playlist URL is selected
- `mpv` starts playback

## 🔩 How It Works
- `SearchService.search_videos(query)`: Calls the API and returns a list of `Video` objects. Saves JSON to `SEARCH_RESULTS_FILE`.
- `VideoService.fetch_video_data(short_uuid)`: Fetches full metadata for a specific video. Saves JSON to `VIDEO_DATA_FILE`.
- `PlaylistService.extract_playlist(video_data)`: Finds a playlist that has separate audio and video tracks and extracts resolutions.
- `PlayerService.play(url)`: Launches `mpv` to play the HLS master playlist URL.

## 🧰 Troubleshooting
- If playback fails, confirm `mpv` is installed and accessible from your terminal.
- API availability can vary; if searches return empty, try different queries.
- If JSON files become large, you can delete them; they will be regenerated on next run.

## 👩‍💻 Development
- Optional linting/formatting:
  ```bash
  pip install ruff black
  ruff check .
  black .
  ```