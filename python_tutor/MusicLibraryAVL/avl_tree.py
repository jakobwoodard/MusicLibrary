from genre_hierarchy import genre_hierarchy


class AVLNode:
    def __init__(self, song):
        self.song = song
        self.genre = song["genre"]
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, song):
        if not root:
            return AVLNode(song)
        if song["genre"] < root.genre:
            root.left = self.insert(root.left, song)
        else:
            root.right = self.insert(root.right, song)
        return self._balance_tree(root)

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _balance_tree(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.song)
            result = result + self.inorder_traversal(root.right)
        return result

    def search_by_genre(self, root, genre):
        parent_genre = self._find_parent_genre(genre)
        return self._search_by_parent_genre(root, parent_genre)

    def _search_by_parent_genre(self, root, parent_genre):
        if not root:
            return []
        songs = [root.song] if self._is_subgenre(root.genre, parent_genre) else []
        return (
            songs
            + self._search_by_parent_genre(root.left, parent_genre)
            + self._search_by_parent_genre(root.right, parent_genre)
        )

    def _find_parent_genre(self, genre, hierarchy=genre_hierarchy["Music"]):
        for parent, children in hierarchy.items():
            if genre == parent or genre in children:
                return parent
            for child, grandchildren in children.items():
                if genre == child or genre in grandchildren:
                    return parent
        return genre

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
