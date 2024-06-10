class MyQueue:
    def __init__(self):
        self.queue = []

    def queue_size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def add(self, item):
        self.queue.append(item)

    def remove(self, item):
        self.queue.remove(item)

    def put(self, index: int, item: any):
        self.queue.insert(index, item)

    def delete_by_index(self, index: int):
        return self.queue.pop(index)
