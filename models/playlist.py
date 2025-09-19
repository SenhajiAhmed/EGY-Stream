class Playlist:
    def __init__(self, master_url, resolutions):
        self.master_url = master_url
        self.resolutions = resolutions or []

    def display_resolutions(self):
        if not self.resolutions:
            return "No resolution info available"
        return ", ".join(
            [f"{r['label']} ({r['width']}x{r['height']})" for r in self.resolutions]
        )
