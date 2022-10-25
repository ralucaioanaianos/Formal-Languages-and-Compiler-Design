class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self._hashTable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def print_hashtable(self):
        for index in range(self._capacity):
            print("index = ", index)
            node = self._hashTable[index]
            while node is not None:
                print("node ", node.key)
                node = node.next
        print()


    def hash_function(self, key):
        letter_sum = 0
        for letter in key:
            letter_sum += ord(letter)
        return letter_sum % self._capacity

    def insert_data(self, key):
        print("to insert: ", key)
        self._size += 1
        index = self.hash_function(key)
        node = self._hashTable[index]
        if node is None:
            self._hashTable[index] = Node(key)
            print("inserted on position ", index)
            self.print_hashtable()
            return
        previous = node
        while node is not None:
            previous = node
            node = node.next
        previous.next = Node(key)
        print("inserted on position ", index)
        self.print_hashtable()
        return index

    def find_data(self, key):
        index = self.hash_function(key)
        node = self._hashTable[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            print("not found")
            return None
        else:
            print("found, index = ", index)
            return index





