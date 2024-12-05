from music_library import MusicLibrary
from song import Song


def main():
    library = MusicLibrary()

    # Load songs from the file
    library.load_songs_from_file("songs.json")
    print("All songs in the library:")
    library.display_all_songs()

    ############################################################

    # Binary search demonstration (from previous lab)
    library.sort_by_title()
    print("\nBinary Search Demonstration:")
    search_title = "Go Crazy"
    result = library.binary_search(search_title)
    if result:
        print(f"Found: {result}")
    else:
        print(f"\n'{search_title}' not found.")

    search_title = "Imaginary Song"
    result = library.binary_search(search_title)
    if result:
        print(f"\nFound: {result}")
    else:
        print(f"\n'{search_title}' not found.")

    print("--------------------------------------------------------")

    # Test QuickSort by Duration
    library.display_songs_sorted_by_duration()

    test_quick_sort()


def test_quick_sort():

    library = MusicLibrary()
    library.add_song(Song("Song 3", "Artist", duration=160))
    library.add_song(Song("Song 2", "Artist", duration=160))
    library.add_song(Song("Song 5", "Artist", duration=160))
    library.add_song(Song("Song 1", "Artist", duration=160))
    library.add_song(Song("Song 4", "Artist", duration=160))
    library.display_songs_sorted_by_duration()

    library_2 = MusicLibrary()
    library_2.add_song(Song("Song 3", "Artist", duration=160))
    library_2.add_song(Song("Song 2", "Artist", duration=161))
    library_2.add_song(Song("Song 5", "Artist", duration=162))
    library_2.add_song(Song("Song 1", "Artist", duration=163))
    library_2.add_song(Song("Song 4", "Artist", duration=164))
    library_2.display_songs_sorted_by_duration()

    library_3 = MusicLibrary()
    library_3.add_song(Song("Song 3", "Artist", duration=164))
    library_3.add_song(Song("Song 2", "Artist", duration=163))
    library_3.add_song(Song("Song 5", "Artist", duration=162))
    library_3.add_song(Song("Song 1", "Artist", duration=161))
    library_3.add_song(Song("Song 4", "Artist", duration=160))
    library_3.display_songs_sorted_by_duration()

    library_4 = MusicLibrary()
    library_4.add_song(Song("Song 3", "Artist", duration=1))
    library_4.add_song(Song("Song 2", "Artist", duration=116))
    library_4.add_song(Song("Song 5", "Artist", duration=17000))
    library_4.add_song(Song("Song 1", "Artist", duration=60))
    library_4.add_song(Song("Song 4", "Artist", duration=160))
    library_4.display_songs_sorted_by_duration()


if __name__ == "__main__":
    main()
