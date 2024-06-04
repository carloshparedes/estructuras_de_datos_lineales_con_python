class listQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse(self):
        total_items = self.size

        for i in range(total_items):
            print(self.items[i])

food = listQueue()
food.enqueue('apple')
food.enqueue('banana')
food.enqueue('cherry')
print(f'food.traverse() : ', food.traverse())  # Output: apple, banana, cherry
food.dequeue()
print(f'food.traverse() : ', food.traverse())  # Output: apple, banana, cherry