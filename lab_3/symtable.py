from hashtable import HashTable


class SymTable:

    identifiers = HashTable(100)
    constants = HashTable(100)

    def getIdentifiers(self):
        return self.identifiers

    def getConstants(self):
        return self.constants

    def addIdentifierToTable(self, key):
        return self.identifiers.insert_data(key)

    def addConstantToTable(self, key):
        return self.constants.insert_data(key)

    def getIdentifierPosition(self, key):
        return self.identifiers.find_data(key)

    def getConstantPosition(self, key):
        return self.constants.find_data(key)

    def __str__(self):
        return "SymTable{" + "identifiers = " + self.identifiers.__str__() + "constants = " + self.constants.__str__() + "}"
