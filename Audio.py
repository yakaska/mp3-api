class Track:
    title = "Unknown"
    artist = "Unknown"
    url = "unknown"
    track_cover = "unknown"
    duration = 0

    def __init__(self, title, artist, url, track_cover, duration):
        self.title = title
        self.artist = artist
        self.url = url
        self.track_cover = track_cover
        self.duration = duration

    def serialize(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "url": self.url,
            "track_cover": self.track_cover,
            "duration": self.duration
        }
