class Node:
    def __init__(self, id, value, height, parent_key):
        self.id = id
        self.value = value
        self.height = height
        self.parent_key = parent_key

    def __str__(self):
        return f'id: {self.id} - value: {self.value} - height: {self.height} - parent_key: {self.parent_key}'
