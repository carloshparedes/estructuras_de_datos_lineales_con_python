from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0   

    def append(self, data):
        node  = Node(data)
        if self.tail is None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def get_size(self):
        return self.size
    
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return current.data
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')
    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

print('-' * 30)
playlist = SinglyLinkedList()
playlist.append('Song 1')
playlist.append('Song 2')
playlist.append('Song 3')
current_song = playlist.tail

def print_playlist_and_current_song(playlist, current_song):
    print("Playlist:")
    for song in playlist.iter():
        print(song)

    print("\nCurrent song:")
    print(current_song.data)

print_playlist_and_current_song(playlist, current_song)

print('-' * 30)

# delete a song method
#playlist.clear()

#iterating over the playlist method
for song in playlist.iter():
    print(song)

# search for a song method
playlist.search('Song 3') 

