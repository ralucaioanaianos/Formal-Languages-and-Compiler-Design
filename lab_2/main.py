# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from hashtable_constants import HashTable


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    identifiersTable = HashTable(10)
    constantsTable = HashTable(10)

    identifiersTable.insert_data("abc")
    identifiersTable.insert_data("cde")
    identifiersTable.insert_data("cba")

    identifiersTable.find_data("abc")
    identifiersTable.find_data("cde")
    identifiersTable.find_data("cba")
    identifiersTable.find_data("aaa")

    constantsTable.insert_data("aaa")
    constantsTable.insert_data("bbb")
    constantsTable.insert_data("ccc")

    constantsTable.find_data("ccc")
    constantsTable.find_data("ddd")
    constantsTable.find_data("aaa")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
