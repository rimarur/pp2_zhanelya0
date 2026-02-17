class Playlist:
    def __init__(self, song):
        self.song = song
        self.songs = []
    def add_songs(self, song):
        self.songs.append(song)
        print(f"Added: {song}")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        print(f"Removed: {song}")
    def show(self):
        print(f"Playlist: {self.song}")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favs")
my_playlist.add_songs("Lol")
my_playlist.add_songs("Kek")
my_playlist.show()


        