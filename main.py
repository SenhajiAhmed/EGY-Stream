from utils.logger import setup_logger
from services.search_service import SearchService
from services.video_service import VideoService
from services.playlist_service import PlaylistService
from services.player_service import PlayerService

def main():
    logger = setup_logger()

    # Step 1: Search videos
    search_service = SearchService(logger)
    query = input("Enter search query: ")
    videos = search_service.search_videos(query)

    if not videos:
        return

    # Step 2: Choose video
    for idx, v in enumerate(videos, 1):
        print(f"{idx}. {v}")
    choice = int(input("Choose a video: ")) - 1
    selected = videos[choice]

    # Step 3: Get video details
    video_service = VideoService(logger)
    video_data = video_service.fetch_video_data(selected.short_uuid)

    # Step 4: Extract playlist
    playlist_service = PlaylistService(logger)
    playlist = playlist_service.extract_playlist(video_data)

    if playlist:
        print(f"\nMaster Playlist: {playlist.master_url}")
        print(f"Resolutions: {playlist.display_resolutions()}")

        # Step 5: Play with mpv
        player = PlayerService(logger)
        player.play(playlist.master_url)

if __name__ == "__main__":
    main()
