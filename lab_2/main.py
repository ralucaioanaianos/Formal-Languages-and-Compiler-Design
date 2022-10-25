from hashtable import HashTable


if __name__ == '__main__':
    identifiersTable = HashTable(10)
    constantsTable = HashTable(10)

    print("inserted on position: ", identifiersTable.insert_data("abc"), "\n")
    print(identifiersTable.__str__())
    print("inserted on position: ", identifiersTable.insert_data("cde"), "\n")
    print(identifiersTable.__str__())
    print("inserted on position: ", identifiersTable.insert_data("cba"), "\n")
    print(identifiersTable.__str__())

    print("found on position: ", identifiersTable.find_data("abc"), "\n")
    print("found on position: ", identifiersTable.find_data("cde"), "\n")
    print("found on position: ", identifiersTable.find_data("cba"), "\n")
    print("found on position: ", identifiersTable.find_data("aaa"), "\n")

    print("inserted on position: ", constantsTable.insert_data("aaa"), "\n")
    print(constantsTable.__str__())
    print("inserted on position: ", constantsTable.insert_data("bbb"), "\n")
    print(constantsTable.__str__())
    print("inserted on position: ", constantsTable.insert_data("ccc"), "\n")
    print(constantsTable.__str__())

    print("found on position: ", constantsTable.find_data("ccc"), "\n")
    print("found on position: ", constantsTable.find_data("ddd"), "\n")
    print("found on position: ", constantsTable.find_data("aaa"), "\n")
