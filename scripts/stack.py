from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            return 'Stack is empty'
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return 'Stack is empty'
    
    def clear(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

food = Stack()
food.push('apple')
food.push('banana')
food.push('cherry')

print(f'food.pop() : ', food.pop())  # Output: cherry
print(f'food.peek() : ', food.peek())  # Output: banana
print(f'food.clear() : ', food.clear())  # Output: None

