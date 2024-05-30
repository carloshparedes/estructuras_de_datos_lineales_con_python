class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

'''
print('-' * 30)

# Create the nodes (processes)
process1 = Node("Start")
process2 = Node("Load data")
process3 = Node("Process data")
process4 = Node("Save results")
process5 = Node("End")

# Link the nodes
process1.next = process2
process2.next = process3
process3.next = process4
process4.next = process5

# Print the process chain
current_node = process1
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
    
print('-' * 30)

'''

'''
node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

print(f'dato del node1: {node1.data}')
print(f'dato del node2: {node2.data}')
print(f'dato del node3: {node3.data}')
print(f'next del node1 Node(1, node2): {node1.next.data}')
print(f'next del node2 Node(2, node3): {node2.next.data}')
print(f'next del node3 Node(3, None): {node3.next}')

print('-' * 30)

for count in range(1, 5):
    head = None
    head = Node(count, head)
    print(f'head.data: {head.data}')
while head is not None:
    print(head.data)
    head = head.next
'''
