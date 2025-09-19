from models.playlist import Playlist

class PlaylistService:
    def __init__(self, logger):
        self.logger = logger

    def extract_playlist(self, video_data):
        playlists = video_data.get("streamingPlaylists", [])
        for playlist in playlists:
            has_audio = any(f.get("hasAudio") and not f.get("hasVideo") for f in playlist.get("files", []))
            has_video = any(f.get("hasVideo") and not f.get("hasAudio") for f in playlist.get("files", []))
            if has_audio and has_video:
                resolutions = []
                for f in playlist.get("files", []):
                    if f.get("hasVideo") and not f.get("hasAudio"):
                        resolutions.append({
                            "label": f.get("resolution", {}).get("label", "Unknown"),
                            "width": f.get("width", 0),
                            "height": f.get("height", 0),
                            "size": f.get("size", 0),
                            "fps": f.get("fps", 0)
                        })
                return Playlist(playlist.get("playlistUrl"), resolutions)
        self.logger.warning("No combined audio+video streams found")
        return None
