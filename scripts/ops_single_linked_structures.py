from  node import Node
 
head = None

for count in range(1, 6):
    head = Node(count, head)
    print(f'count {count} head.data {head.data} head.next {head.next.data if head.next else None}')

print('-' * 10)

while head != None:
    print(f'head.data: {head.data}')
    if head.next is None:
        print(f'Next node is {head.next}, this is the last node.')
    head = head.next

print('-' * 10)

probe = head
# print(f'probe: {probe}')

target_item = 1
while probe is not None and target_item != probe.data:
    print(f'probe.data: {probe.data}')
    probe = probe.next
    print(f'probe: {probe}')

if probe is not None:
    print(f'Found item {target_item}')
else:    
    print(f'target_item {target_item} not found')

print('-' * 10)

probe = head
target_item = 3
new_item = "Z"

while probe is not None and target_item != probe.data:
    probe = probe.next

if probe is not None:
    probe.data = new_item
    print(f'target_item {target_item} has been replaced by {new_item}')
else:
    print(f'target_item {target_item} not found')

print('-' * 10)

head = Node("Start", head)
new_node = Node("New")

if head is not None:
    head = new_node
    print(f'new_node.data: {new_node.data}')
else:
    probe = head
    while probe.next is not None:
        probe = probe.next
    probe.next = new_node
    print(f'new_node.data: {new_node.data}')

print('-' * 10)

# remove_item = head.data
# head = head.next
# print(f'remove_item {remove_item} has been removed')

remove_item = head.data
if head.next is None:
    head = None 
    print(f'remove_item {remove_item} has been removed')
else:    
    probe = head
    while probe.next.next is not None:
        probe = probe.next
    remove_item = probe.next.data
    probe.next = None
    print(f'remove_item {remove_item} has been removed')

print('-' * 10)

new_item = input("Enter the new item: ")
index = int(input("Enter the index: "))

if head is None or index == 0:
    head = Node(new_item, head)
    print(f'new_item {new_item} has been added at the beginning')
else:
    probe = head
    while index > 1 and probe.next is not None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)
    print(f'new_item {new_item} has been added at index {index}')
