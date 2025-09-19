class Video:
    def __init__(self, name, short_uuid, url=None):
        self.name = name
        self.short_uuid = short_uuid
        self.url = url

    def __str__(self):
        return f"{self.name} ({self.short_uuid})"
