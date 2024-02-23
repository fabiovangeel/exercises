class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def next(self):
        self.queue.remove(0)
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie')  # And Charlie as third

queue.next()   # Alice arrived first, so she's the first to be served next
queue.next()   # This must return Bob
queue.next()   # Finally, it's Charlie's turn
