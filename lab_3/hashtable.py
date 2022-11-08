class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self._hashTable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        to_print = ""
        for index in range(self._capacity):
            to_print += "index = " + str(index) + ": "
            node = self._hashTable[index]
            while node is not None:
                to_print += str(node.key) + ' '
                node = node.next
            to_print += "\n"
        to_print += "\n"
        return to_print + "\n"

    def hash_function(self, key):
        letter_sum = 0
        for letter in key:
            letter_sum += ord(letter)
        return letter_sum % self._capacity

    def insert_data(self, key):
        self._size += 1
        if self._size >= self._capacity-1:
            self._capacity += self._capacity
        index = self.hash_function(key)
        node = self._hashTable[index]
        if node is None:
            self._hashTable[index] = Node(key)
            return index
        previous = node
        while node is not None:
            previous = node
            node = node.next
        previous.next = Node(key)
        return index

    def find_data(self, key):
        index = self.hash_function(key)
        node = self._hashTable[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return index
