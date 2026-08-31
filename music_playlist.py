class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        return f"Added '{song}' to {self.name}."

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            return f"Removed '{song}' from {self.name}."
        return f"'{song}' not found in playlist."

    def show_songs(self):
        if not self.songs:
            return f"Playlist {self.name} is empty."
        return f"Songs in {self.name}: {', '.join(self.songs)}"

# Creating an object
my_playlist = Playlist("Road Trip Favorites")

# Interacting with the object
print(my_playlist.add_song("Bohemian Rhapsody"))  # Output: Added 'Bohemian Rhapsody' to Road Trip Favorites.
print(my_playlist.add_song("Hotel California"))   # Output: Added 'Hotel California' to Road Trip Favorites.
print(my_playlist.show_songs())                   # Output: Songs in Road Trip Favorites: Bohemian Rhapsody, Hotel California
print(my_playlist.remove_song("Bohemian Rhapsody")) # Output: Removed 'Bohemian Rhapsody' from Road Trip Favorites.
