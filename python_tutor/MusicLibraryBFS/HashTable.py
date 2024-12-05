class HashTable:

    def __init__(self):
        self.table = {}

    def add(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)

    def display_all(self):
        for key, value in self.table.items():
            print(f"{key}: {value}")
