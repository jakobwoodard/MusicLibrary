import json
from song import Song
from HashTable import HashTable
from collections import deque, defaultdict
import heapq


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Dictionary to store the graph
        self.weights = {}  # Dictionary to store edge weights

    def add_edge(self, song_from, song_to):
        self.graph[song_from].append(song_to)  # Add connection for the song_from
        self.graph[song_to].append(song_from)  # Make graph unidirectional

    def display_adjacency_list(self):
        for song, connections in self.graph.items():
            print(f"{song}: {connections}")

    def add_weighted_edge(self, song_from, song_to, weight):
        self.graph[song_from].append(song_to)
        self.graph[song_to].append(song_from)  # Assuming the graph is undirected
        self.weights[(song_from, song_to)] = weight
        self.weights[(song_to, song_from)] = weight

    def calculate_weight(self, song1, song2):
        danceability_diff = abs(song1.danceability - song2.danceability) / 1
        energy_diff = abs(song1.energy - song2.energy) / 1
        valence_diff = abs(song1.valence - song2.valence) / 1
        duration_diff = abs(song1.duration - song2.duration) / 300
        score_diff = abs(song1.score - song2.score) / 100

        weight = (
            danceability_diff * 3
            + energy_diff * 3
            + valence_diff * 3
            + duration_diff
            + score_diff
        ) / 11
        return weight

    def dijkstra(self, start):
        pq = [(0, start)]
        distances = {start: 0}
        pred = {start: None}
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor in self.graph[current_vertex]:
                weight = self.weights.get((current_vertex, neighbor), 1)
                distance = current_distance + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    priority = distance
                    heapq.heappush(pq, (priority, neighbor))
                    pred[neighbor] = current_vertex
        return distances, pred

    def shortest_path(self, start, end):
        distances, pred = self.dijkstra(start)
        path = []
        current = end

        while current is not None:
            path.append(current)
            try:
                current = pred[current]
            except:
                return None
        path.reverse()
        return path

    def display_graph(self):
        print("Graph Representation:")
        for song, connections in self.graph.items():
            conn_details = [
                f"{conn} (weight: {self.weights.get((song, conn), 1):.2f})"
                for conn in connections
            ]
            print(f"{song}: {', '.join(conn_details)}")


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

    def build_weighted_graph(self):
        for i in range(len(self.songs)):
            for j in range(i + 1, len(self.songs)):
                song1 = self.songs[i]
                song2 = self.songs[j]
                weight = self.graph.calculate_weight(song1, song2)
                self.graph.add_weighted_edge(song1.title, song2.title, weight)
            # Ensure intermediate steps by connecting every second song
            # Naturally setting broad but valid connections
            if i < len(self.songs) - 2:
                song1 = self.songs[i]
                song2 = self.songs[i + 2]
                weight = self.graph.calculate_weight(song1, song2)
                self.graph.add_weighted_edge(song1.title, song2.title, weight)

    def display_shortest_path_playlist(self, start_title, end_title):
        path = self.graph.shortest_path(start_title, end_title)
        if path:
            print(f"Shortest path playlist from '{start_title}' to '{end_title}':")
            for song_title in path:
                print(song_title)
        else:
            print(f"No path found from '{start_title}' to '{end_title}'")

    def fit_most_songs(self, playlist_time):
        # Convert minutes to seconds
        available_time = playlist_time * 60
        # Sort songs by duration in ascending order
        sorted_songs = sorted(self.songs, key=lambda song: song.duration)

        total_duration = 0
        playlist = []
        for song in sorted_songs:
            if total_duration + song.duration <= available_time:
                playlist.append(song)
                total_duration += song.duration
            else:
                break
        print(
            f"\nPlaylist fitting in {playlist_time} minutes ({available_time} seconds):"
        )
        self.display_songs(playlist)

        minutes = total_duration // 60
        seconds = total_duration % 60
        print(f"\nPlaylist length: {minutes} minutes and {seconds} seconds")
