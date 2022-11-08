from hashtable import HashTable
from scanner import Scanner

if __name__ == '__main__':
    scanner1 = Scanner("p1.txt")
    print(scanner1.readFile())
    scanner1err = Scanner("p1err.txt")
    print(scanner1err.readFile())
    scanner2 = Scanner("p2.txt")
    print(scanner2.readFile())
    scanner3 = Scanner("p3.txt")
    print(scanner3.readFile())





