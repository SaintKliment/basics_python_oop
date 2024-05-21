import random
class MusicAlbum:
    def __init__(self, titles, artist, release_year, genre, playlist):
        self.titles = titles
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.playlist = playlist

    def play_random_track(self):
        self.random_song = random.choice(self.titles)
        
        return (f"Название песни: {self.random_song} \nИсполнитель: {self.artist} \nГод релиза: {self.release_year} \nЖанр: {self.genre} \nПлейлист: {self.playlist}") 

m = MusicAlbum(['one', 'two', 'three'], 'ckiloven', 2007, 'RAP', 'NoHomo')
print(m.play_random_track())