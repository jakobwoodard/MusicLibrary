class Song:
    def __init__(
        self,
        title,
        artist,
        score=0,
        genre="",
        danceability=0.0,
        energy=0.0,
        valence=0.0,
        duration=0,
    ):
        self.title = title
        self.artist = artist
        self.score = score
        self.genre = genre
        self.danceability = danceability
        self.energy = energy
        self.valence = valence
        self.duration = duration

    def __str__(self):
        return (
            f"{self.title[:22]+'...' if len(self.title) > 25 else self.title:25} "
            f"{self.artist[:17]+'...' if len(self.artist) > 20 else self.artist:20} "
            f"{self.score:<5} "
            f"{self.genre[:7]+'...' if len(self.genre) > 10 else self.genre:10} "
            f"{self.danceability:<12.2f} "
            f"{self.energy:<10.2f} "
            f"{self.valence:<10.2f} "
            f"{self.duration:<8}"
        )

    def __lt__(self, other):
        return self.title < other.title
