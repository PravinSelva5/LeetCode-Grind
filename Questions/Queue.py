class QueueLine:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
