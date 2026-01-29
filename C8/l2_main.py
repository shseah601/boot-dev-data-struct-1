class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None

        item = self.items[0]

        for i in range(len(self.items) - 1):
            self.items[i] = self.items[i + 1]

        self.items.pop()

        return item

    def peek(self):
        if len(self.items) == 0:
            return None

        return self.items[0]

    def size(self):
        return len(self.items)
