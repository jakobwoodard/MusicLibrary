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

    print("--------------------------------------------------------")

    # Adding BFS by Song demo that demonstrates the BFS functionality:
    start_song = "Go Crazy"
    print(f"\nBFS by starting song -> '{start_song}'")
    library.build_graph()
    library.display_bfs_by_song(start_song)

    # Test cases for BFS file to include these test cases. For example:
    test_songs = [
        "Shape of You",
        "Imaginary Song",
        "Collaboration Song",
        "Isolated Song",
    ]
    for song in test_songs:
        print(f"\nBFS starting from '{song}':")
        library.display_bfs_by_song(song)

    library.display_bfs_by_song("For The Night")
    print()
    library.display_bfs_by_song("Calling My Phone")
    print()
    library.display_bfs_by_song("Stay")
    print()
    library.display_bfs_by_song("Good Days")
    print()

    # Build weighted graph for Dijkstra's algorithm
    library.build_weighted_graph()
    # Demonstrate finding the shortest path playlist between two songs
    start_song = "Hotline Bling"
    end_song = "Shape of You"
    print("\nShortest Path Playlist Based on Similarity:")
    library.display_shortest_path_playlist(start_song, end_song)

    # Test cases for Dijkstra's algorithm
    test_cases = [
        ("Shape of You", "Blinding Lights"),  # Similar pop songs
        ("Shape of You", "Bohemian Rhapsody"),  # Different genres
        ("Shape of You", "Shape of You"),  # Same song
        ("Imaginary Song", "Shape of You"),  # Non-existent song
    ]
    for start, end in test_cases:
        print(f"\nFinding shortest path from '{start}' to '{end}':")
        library.display_shortest_path_playlist(start, end)


if __name__ == "__main__":
    main()
