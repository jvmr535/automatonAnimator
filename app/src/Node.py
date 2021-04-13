class Node:
    def __init__(self, id: str, value: str, height: str, parent_id: str):
        self.id = id
        self.value = value
        self.height = height
        self.parent_id = parent_id

    def __str__(self):
        return f'id: {self.id} - value: {self.value} - height: {self.height} - parent id: {self.parent_id}'
