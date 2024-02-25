class CircularBuffer:
    def __init__(self, max_length):
        self.max_length = max_length
        self.list = []

    def add(self, item):
        if len(self.list) < self.max_length:
            self.list.append(item)
        else:
            self.list.pop(0)
            self.list.append(item)

    def __getitem__(self, index):
        return self.list[index]

    def __len__(self):
        return len(self.list)
