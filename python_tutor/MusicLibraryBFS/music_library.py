import json
from song import Song
from HashTable import HashTable
from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Dictionary to store the graph

    def add_edge(self, song_from, song_to):
        self.graph[song_from].append(song_to)  # Add connection for the song_from

    def display_adjacency_list(self):
        for song, connections in self.graph.items():
            print(f"{song}: {connections}")


class MusicLibrary:

    def __init__(self):
        self.songs = []
        self.song_table = HashTable()
        self.graph = Graph()

    def add_song(self, song):
        self.songs.append(song)
        self.songs.sort()
        self.song_table.add(song.title, song)

    def load_songs_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            for item in data["songs"]:
                song = Song(
                    title=item["title"],
                    artist=item["artist"],
                    score=item.get("score", 0),
                    genre=item.get("genre", ""),
                    danceability=item.get("danceability", 0.0),
                    energy=item.get("energy", 0.0),
                    valence=item.get("valence", 0.0),
                    duration=item.get("duration", 0),
                )
                self.add_song(song)

    def display_all_songs(self):
        headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
        print(headers)
        print("-" * len(headers))
        for song in self.songs:
            print(song)

    def sort_by_title(self):
        self.songs.sort(key=lambda x: x.title)

    def binary_search(self, title):
        low, high = 0, len(self.songs) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.songs[mid].title == title:
                return self.songs[mid]
            elif self.songs[mid].title < title:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def selection_sort_by_score(self):
        for i in range(len(self.songs)):
            max_idx = i
            for j in range(i + 1, len(self.songs)):
                if self.songs[j].score > self.songs[max_idx].score:
                    max_idx = j
            self.songs[i], self.songs[max_idx] = self.songs[max_idx], self.songs[i]

    def selection_sort_by_danceability(self):
        for i in range(len(self.songs)):
            max_idx = i
            for j in range(i + 1, len(self.songs)):
                if self.songs[j].danceability > self.songs[max_idx].danceability:
                    max_idx = j
            self.songs[i], self.songs[max_idx] = self.songs[max_idx], self.songs[i]

    def top_songs_by_score(self, n=10):
        self.selection_sort_by_score()
        print("\nTop Songs by Score:")
        self.display_songs(self.songs[:n])

    def top_songs_by_danceability(self, n=10):
        self.selection_sort_by_danceability()
        print("\nTop Songs by Danceability:")
        self.display_songs(self.songs[:n])

    def display_songs(self, songs):
        headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
        print(headers)
        print("-" * len(headers))
        for song in songs:
            print(song)

    def recursive_display(self, index=0):
        if index == 0:
            headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
            print(headers)
            print("-" * len(headers))
            print("-" * len(headers))
        if index == len(self.songs):
            return
        print(self.songs[index])
        self.recursive_display(index + 1)

    def recursive_search(self, title, low=0, high=None):
        if high is None:
            high = len(self.songs) - 1
        if low > high:
            return None
        mid = (low + high) // 2
        if self.songs[mid].title == title:
            return self.songs[mid]
        elif self.songs[mid].title < title:
            return self.recursive_search(title, mid + 1, high)
        else:
            return self.recursive_search(title, low, mid - 1)

    def _quicksort_by_duration(self, array, low, high):
        if low < high:
            pi = self._partition(array, low, high)
            self._quicksort_by_duration(array, low, pi - 1)
            self._quicksort_by_duration(array, pi + 1, high)

    def _partition(self, array, low, high):
        pivot = array[high].duration
        i = low - 1
        for j in range(low, high):
            if array[j].duration <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def sort_by_duration_quick(self):
        self._quicksort_by_duration(self.songs, 0, len(self.songs) - 1)

    def display_songs_sorted_by_duration(self):
        self.sort_by_duration_quick()
        print("\nSongs sorted by Duration using QuickSort:")
        self.display_all_songs()

    def search_in_hashtable(self, title):
        return self.song_table.get(title)

    def display_hashtable_contents(self):
        print("\nHashtable contents:")
        self.song_table.display_all()

    def build_graph(self):
        artist_to_songs = defaultdict(list)
        for song in self.songs:
            artists = song.artist.split(", ")
            for artist in artists:
                artist_to_songs[artist].append(song.title)
        for songs in artist_to_songs.values():
            for i in range(len(songs)):
                for j in range(len(songs)):
                    if i != j:
                        self.graph.add_edge(songs[i], songs[j])

    def bfs_by_song(self, start_song):
        visited = set()
        queue = deque([start_song])
        related_songs = []
        while queue:
            current_song = queue.popleft()
            if current_song not in visited:
                visited.add(current_song)
                if current_song in self.graph.graph:
                    for neighbor in self.graph.graph[current_song]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                related_songs.append(current_song)
        return related_songs

    def display_bfs_by_song(self, start_song):
        print("Adjacency List:")
        self.graph.display_adjacency_list()
        related_songs = self.bfs_by_song(start_song)
        print(f"\nBFS starting from '{start_song}':")
        for song in related_songs:
            print(song)
