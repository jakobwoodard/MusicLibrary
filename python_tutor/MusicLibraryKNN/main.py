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

    print("--------------------------------------------------------")

    # Demonstrate fitting most songs into a given time
    playlist_time = 22  # Example: 22 minutes
    print(f"\nFitting most songs into {playlist_time} minutes playlist:")
    library.fit_most_songs(playlist_time)

    # Test cases for Greedy algorithm
    test_times = [1, 5, 22, 60, 1000]
    for time in test_times:
        print(f"\nTesting playlist creation for {time} minutes:")
        library.fit_most_songs(time)

    # Demonstrate fitting most songs into a given time
    playlist_time = 1  # Example: 1 minutes
    print(f"\nFitting most songs into {playlist_time} minutes playlist:")
    library.fit_most_songs(playlist_time)

    # Demonstrate fitting most songs into a given time
    playlist_time = 1000  # Example: 1000 minutes
    print(f"\nFitting most songs into {playlist_time} minutes playlist:")
    library.fit_most_songs(playlist_time)

    # Demonstrate fitting most songs into a given time
    playlist_time = 2.2  # Example: 2.2 minutes
    print(f"\nFitting most songs into {playlist_time} minutes playlist:")
    library.fit_most_songs(playlist_time)

    new_library = MusicLibrary()
    new_library.add_song(Song("Sicko Mode", "Travis Scott", duration=321))
    new_library.add_song(Song("Good Days", "SZA", duration=277))
    new_library.add_song(Song("Hotline Bling", "Drake", duration=267))
    new_library.fit_most_songs(12)

    new_library_2 = MusicLibrary()
    new_library_2.add_song(Song("Mood", "24kGoldn, Iann Dior", duration=140))
    new_library_2.add_song(Song("WHATS POPPIN", "Jack Harlow", duration=141))
    new_library_2.add_song(Song("Test Song", "Artist 3", duration=60))
    new_library_2.fit_most_songs(200 / 60)

    print("--------------------------------------------------------")

    # Demonstrate fitting highest value of songs into a given time using dynamic programming
    playlist_time = 22  # Example: 22 minutes
    print(
        f"\nFitting highest value songs into {playlist_time} minutes playlist (Dynamic Programming):"
    )
    library.fit_highest_value_songs(playlist_time)

    # Test cases for Dynamic Programming algorithm
    test_times = [1, 5, 22, 60, 1000]
    for time in test_times:
        print(f"\nTesting optimal playlist creation for {time} minutes:")
        library.fit_highest_value_songs(time)

    # Test with custom song set
    custom_songs = [
        Song("Long High Score", "Artist1", score=100, duration=500),
        Song("Short Low Score", "Artist2", score=10, duration=50),
        Song("Medium Score", "Artist3", score=50, duration=200),
    ]
    custom_library = MusicLibrary()
    for song in custom_songs:
        custom_library.add_song(song)
    custom_library.fit_highest_value_songs(10)  # 10 minutes

    # Demonstrate kNN
    target_song = "Blinding Lights"
    k = 5
    print(f"\nk-Nearest Neighbors (k={k}) for '{target_song}':")
    library.display_knn(target_song, k)

    k_values = [1, 3, 10, 1000]
    for value in k_values:
        for song in test_songs:
            library.display_knn(song, value)


if __name__ == "__main__":
    main()
