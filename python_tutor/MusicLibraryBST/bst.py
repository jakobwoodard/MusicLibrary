from genre_hierarchy import genre_hierarchy


class GenreNode:
    def __init__(self, genre):
        self.genre = genre
        self.songs = []
        self.left = None
        self.right = None


class GenreBST:
    def __init__(self):
        self.root = None
        self.root = None
        self._build_tree(genre_hierarchy["Music"])

    def _build_tree(self, hierarchy, parent=None):
        if not hierarchy:
            return None
        genres = list(hierarchy.keys())
        mid = len(genres) // 2
        genre = genres[mid]
        node = GenreNode(genre)
        if parent is None:
            self.root = node
        elif genre < parent.genre:
            parent.left = node
        else:
            parent.right = node
        node.left = self._build_tree(
            {k: v for k, v in hierarchy.items() if k < genre}, node
        )
        node.right = self._build_tree(
            {k: v for k, v in hierarchy.items() if k > genre}, node
        )
        for subgenre in hierarchy[genre]:
            self._build_tree({subgenre: hierarchy[genre][subgenre]}, node)
        return node

    def insert(self, song):
        genre = song["genre"]
        parent_genre = self._find_parent_genre(genre)
        self._insert(self.root, parent_genre, song)

    def _insert(self, node, genre, song):
        if node is None:
            return GenreNode(genre)
        if genre == node.genre:
            node.songs.append(song)
        elif genre < node.genre:
            node.left = self._insert(node.left, genre, song)
        else:
            node.right = self._insert(node.right, genre, song)
        return node

    def _find_parent_genre(self, genre, hierarchy=genre_hierarchy["Music"]):
        for parent, children in hierarchy.items():
            if genre == parent or genre in children:
                return parent
            for child, grandchildren in children.items():
                if genre == child or genre in grandchildren:
                    return parent
        return genre  # If no parent found, return the genre itself

    def search(self, genre):
        return self._search(self.root, genre)

    def _search(self, node, genre):
        if node is None:
            return []
        if genre == node.genre:
            return (
                node.songs
                + self._search_subgenres(node.left, genre)
                + self._search_subgenres(node.right, genre)
            )
        elif genre < node.genre:
            return self._search(node.left, genre)
        else:
            return self._search(node.right, genre)

    def _search_subgenres(self, node, parent_genre):
        if node is None:
            return []
        songs = node.songs if self._is_subgenre(node.genre, parent_genre) else []
        return (
            songs
            + self._search_subgenres(node.left, parent_genre)
            + self._search_subgenres(node.right, parent_genre)
        )

    def _is_subgenre(self, genre, parent_genre):
        def check_hierarchy(hierarchy):
            for key, value in hierarchy.items():
                if key == parent_genre:
                    return genre == key or genre in value
                if isinstance(value, dict):
                    if check_hierarchy(value):
                        return True
            return False

        return check_hierarchy(genre_hierarchy["Music"])

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(f"Genre: {node.genre}, Songs: {len(node.songs)}")
            self._inorder_traversal(node.right)
