import subprocess

class PlayerService:
    def __init__(self, logger):
        self.logger = logger

    def play(self, url):
        self.logger.info(f"Playing stream: {url}")
        subprocess.run(["mpv", url])
