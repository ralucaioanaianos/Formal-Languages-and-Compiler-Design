from hashtable import HashTable


class SymTable:

    identifiers = HashTable(10)
    constants = HashTable(10)

    def getIdentifiers(self):
        """
        :return: the table of identifiers
        """
        return self.identifiers

    def getConstants(self):
        """
        :return: the table of constants
        """
        return self.constants

    def addIdentifierToTable(self, key):
        """
        :param key: the key to add to the table of identifiers
        :return: the index where key was inserted in the table of identifiers
        """
        return self.identifiers.insert_data(key)

    def addConstantToTable(self, key):
        """
        :param key: the key to add to the table of constants
        :return: the index where key was inserted in the table of constants
        """
        return self.constants.insert_data(key)

    def getIdentifierPosition(self, key):
        """
        :param key: the key to find in the table of identifiers
        :return: the index where the key is found in the table of identifiers, None if it does not exist
        """
        return self.identifiers.find_data(key)

    def getConstantPosition(self, key):
        """
        :param key: the key to find in the table of constants
        :return: the index where the key is found in the table of constants, None if it does not exist
        """
        return self.constants.find_data(key)

    def __str__(self):
        """
        :return: the string representation of SymTable
        """
        return "SymTable{", \
               "identifiers = ", self.identifiers.__str__(), \
               "constants = ", self.constants.__str__(), \
               "}"
