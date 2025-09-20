# 📺 Video Search & Streaming Project
This project allows you to **search videos**, fetch **metadata and playlists**, and play streams using **mpv**.  
It is refactored into a clean **Object-Oriented Python project** with multiple files and services.  

## 🚀 Features
- 🔍 Search for videos via `ma3ak.top` API  
- 📂 Save search results and video data to JSON files  
- 🎥 Extract **HLS master playlists** that combine audio & video  
- 📊 Display available resolutions (width, height, fps, size)  
- ▶️ Play video streams directly with **mpv**  

## 📂 Project Structure
video_project/
│── main.py
│── config.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── services/
│ ├── search_service.py
│ ├── video_service.py
│ ├── playlist_service.py
│ └── player_service.py
│
├── models/
│ ├── video.py
│ └── playlist.py
│
└── utils/
├── file_manager.py
└── logger.py


## ⚙️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/video_project.git
   cd video_project


pip install -r requirements.txt


▶️ Usage

Run the main script:
python main.py

Steps:

Enter your search query

Choose a video from the list

The script fetches metadata & playlist info

Selects a master playlist URL

Plays the video in mpv