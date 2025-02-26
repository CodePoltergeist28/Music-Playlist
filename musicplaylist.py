import os
import random

class Song:
    """Represents a song with title, artist, and duration."""
    
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration})"

class Playlist(Song):
    """Manages a playlist (add, remove, display, save, load, delete)."""

    def __init__(self, name):
        self.name = name + ".txt"
        self.songs = []
        self.load_playlist()

    def add_song(self):
        """Adds a new song to the playlist."""
        title = input("Enter song title: ").strip()
        artist = input("Enter artist: ").strip()
        duration = input("Enter duration (mm:ss): ").strip()
        
        song = Song(title, artist, duration)
        self.songs.append(song)
        print(f"✅ Added: {song}")

    def remove_song(self):
        """Removes a song by title."""
        title = input("Enter song title to remove: ").strip()
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                print(f"❌ Removed: {song}")
                return
        print("⚠ Song not found.")

    def display_playlist(self):
        """Displays all songs in the playlist."""
        if not self.songs:
            print("📂 Playlist is empty.")
        else:
            print("\n🎵 Playlist:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")

    def save_playlist(self):
        """Saves the playlist to a file."""
        with open(self.name, "w") as file:

            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.duration}\n")
        print(f"💾 Playlist saved as '{self.name}'.")

    def load_playlist(self):
        """Loads an existing playlist from a file if it exists.""" 
        if os.path.exists(self.name):

            with open(self.name, "r") as file:
                for line in file:
                    title, artist, duration = line.strip().split(',')
                    self.songs.append(Song(title, artist, duration))
            print(f"📥 Loaded playlist: {self.name}")
        else:
            print("📂 No existing playlist found. Starting a new one.")

    def delete_playlist(self):
        """Deletes the playlist file from the system.""" 
        if os.path.exists(self.name):
            confirm = input(f"⚠ Are you absolutely sure you want to delete '{self.name}'? (yes/no): ").strip().lower()

            if confirm == "yes":
                os.remove(self.name)
                self.songs = []  # Clear playlist
                print(f"🗑 Playlist '{self.name}' deleted.")
            else:
                print("❌ Playlist deletion canceled.")
        else:
            print("⚠ No playlist file found.")

    def edit_song(self):
        song_title = input("What’s the title of the song you’d like to edit? ").strip()

        for song in self.songs:
            if song.title.lower() == self.title.lower():
                print(f"Editing: {song}")
                song.title = input("New title (leave empty to keep current): ") or song.title
                song.artist = input("New artist (leave empty to keep current): ") or song.artist
                song.duration = input("New duration (leave empty to keep current): ") or song.duration
                print(f"✅ Updated song: {song}")
                return
        print("⚠ Song not found.")
    
    def search_song(self):
        keyword = input("What song title or artist would you like to search for? ").strip().lower()

        results = [song for song in self.songs if keyword in song.title.lower() or keyword in song.artist.lower()]
        if results:
            print("\n🔍 Search Results:")
            for song in results:
                print(f"🎶 {song}")
        else:
            print("⚠ No matching songs found.")
        
    def sort_playlist(self):
        print("\nHow would you like to sort the playlist? 1️⃣ By Title 2️⃣ By Artist 3️⃣ By Duration")
        choice = input("Please enter your choice (1/2/3): ")

        if choice == "1":
            self.songs.sort(key=lambda song: song.title.lower())
        elif choice == "2":
            self.songs.sort(key=lambda song: song.artist.lower())
        elif choice == "3":
            self.songs.sort(key=lambda song: song.duration)
        else:
            print("⚠ Invalid choice.")
            return
        print("✅ Playlist sorted successfully!")

    def shuffle_playlist(self):
        """Randomly shuffles the order of songs in the playlist.""" 
        random.shuffle(self.songs)
        print("🔀 Your playlist has been shuffled!")


def main():
    """Main program loop for the Music Playlist Manager.""" 
    print("🎶 Welcome to the Music Playlist Manager! 🎶")
    playlist_name = input("What would you like to name your playlist? ").strip()

    playlist = Playlist(playlist_name)

    while True:

        print("\nOptions:")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Display Playlist")
        print("4. Edit Song")
        print("5. Save Playlist")
        print("6. Delete Playlist")
        print("7. Search Song")
        print("8. Sort Playlist")
        print("9. Shuffle Playlist")
        print("10. Exit the program")



        choice = input("Enter your choice: ")

        if choice == "1":
            playlist.add_song()
        elif choice == "2":
            playlist.remove_song()
        elif choice == "3":
            playlist.display_playlist()
        elif choice == "4":
            playlist.edit_song()
        elif choice == "5":
            playlist.save_playlist()
        elif choice == "6":
            playlist.delete_playlist()
        elif choice == "7":
            playlist.search_song()
        elif choice == "8":
            playlist.sort_playlist()
        elif choice == "9":
            playlist.shuffle_playlist()
        elif choice == "10":
            exit()
        elif choice == "0":
            print("👋 Thank you for using the Music Playlist Manager. Goodbye!")

            break
        else:
            print("⚠ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
