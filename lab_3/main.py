from finiteautomata import FiniteAutomata
from grammar import Grammar
from hashtable import HashTable
from scanner import Scanner
from ui import UI

if __name__ == '__main__':
    ui = UI()
    ui.run()
    # scanner1 = Scanner("p1.txt")
    # print(scanner1.readFile())
    # scanner1err = Scanner("p1err.txt")
    # print(scanner1err.readFile())
    # scanner2 = Scanner("p2.txt")
    # print(scanner2.readFile())
    # scanner3 = Scanner("p3.txt")
    # print(scanner3.readFile())

    # fa = FiniteAutomata()
    # grammar = Grammar()
    #
    # def printMenu():
    #     print("0. exit")
    #     print("1. display the set of states")
    #     print("2. display the alphabet")
    #     print("3. display all the transitions")
    #     print("4. display the initial state")
    #     print("5. display the set of final states")
    #
    # def displaySetOfStates():
    #     print(fa.displayQ())
    #
    # def displayAlphabet():
    #     print(fa.displayE())
    #
    # def displayTransitions():
    #     print(fa.displayD())
    #
    # def displayInitialState():
    #     print(fa.displayQ0())
    #
    # def displayFinalStates():
    #     print(fa.displayF())


    # while True:
    #     printMenu()
    #     command = input("command: ")
    #     if command == "1":
    #         displaySetOfStates()
    #     elif command == "2":
    #         displayAlphabet()
    #     elif command == "3":
    #         displayTransitions()
    #     elif command == "4":
    #         displayInitialState()
    #     elif command == "5":
    #         displayFinalStates()
    #     elif command == "0":
    #         break
    #     else:
    #         print("invalid command!")
