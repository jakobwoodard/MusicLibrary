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

    # Hashtable demonstrations
    print("\nHashtable Search Example:")
    search_title = "Go Crazy"
    ht_result = library.search_in_hashtable(search_title)
    if ht_result:
        print(f"Found in Hashtable: {ht_result}")
    else:
        print(f"Not found in Hashtable: {search_title}")
    search_title = "Imaginary Song"
    ht_result = library.search_in_hashtable(search_title)
    if ht_result:
        print(f"Found in Hashtable: {ht_result}")
    else:
        print(f"Not found in Hashtable: {search_title}")

    # Additional test cases for hash table
    library.add_song(Song("Artist 1", "Song 1"))
    print(library.search_in_hashtable("Song 1"))
    print(library.search_in_hashtable(""))
    print(library.search_in_hashtable("This is a very long song title"))


if __name__ == "__main__":
    main()
