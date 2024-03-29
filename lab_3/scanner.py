from hashtable import HashTable
import re

from symtable import SymTable


class Scanner:

    separators = []
    operators = []
    reservedWords = []
    pif = []
    symTable = SymTable()
    fileToCheck = ""
    tokens = []

    def __init__(self, fileToCheck):
        self.fileToCheck = fileToCheck
        self.readTokenFile()

    def readFile(self):
        errors = []
        lineNumber = 0
        with open(self.fileToCheck, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                answer = self.tokenizeLine(line)
                if answer is not None:
                    errors.append([lineNumber, answer])
                lineNumber += 1
        f.close()
        self.writeToPifFile()
        self.writeToSTFile()
        return errors

    def readTokenFile(self):
        with open('token.in', 'r') as f:
            f.readline()
            for i in range(17):
                operator = f.readline().strip()
                self.operators.append(operator)
            for i in range(9):
                separator = f.readline().strip()
                if separator == "<space>":
                    separator = " "
                self.separators.append(separator)
            for i in range(22):
                reservedWord = f.readline().strip()
                self.reservedWords.append(reservedWord)

    def writeToSTFile(self):
        with open("ST.out", "w") as f:
            f.write(self.symTable.__str__())
        f.close()

    def writeToPifFile(self):
        with open("pif.out", "w") as f:
            stringToWrite = ""
            for i in range(len(self.pif)):
                if self.pif[i] is not None:
                    stringToWrite += self.pif[i][0].__str__()
                    stringToWrite += " -> "
                    stringToWrite += "("
                    stringToWrite += self.pif[i][1][0].__str__()
                    stringToWrite += ", "
                    stringToWrite += self.pif[i][1][1].__str__()
                    stringToWrite += ")\n"
            f.write(stringToWrite)
            f.close()

    def isReservedWord(self, token: str):
        if token in self.reservedWords:
            if ["token", (-1, token)] not in self.pif:
                self.pif.append(["token", (-1, token)])
            return True
        return False

    def isIdentifier(self, token):
        if re.match(r'([a-zA-Z]|[_])([a-zA-Z]|[0-9]|[_])*$', token) is not None:
            index = self.symTable.addIdentifierToTable(token)
            if ["id", (index, token)] not in self.pif:
                self.pif.append(["id", (index, token)])
            return True
        return False

    def isStringConstant(self, token):
        if re.match(r'^["]([a-zA-Z]|[0-9]|[_])["]$', token):
            if ["stringConstant", [-3, -3]] not in self.pif:
                self.pif.append(["stringConstant", [-3, -3]])
            self.symTable.addConstantToTable(token)
            return True
        return False

    def isConstant(self, token):
        if re.match(r'(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None:
            if ["constant", [-2, -2]] not in self.pif:
                self.pif.append(["constant", [-2, -2]])
            self.symTable.addConstantToTable(token)

            return True
        return False

    def isPartOfOperator(self, char):
        for operator in self.operators:
            if char in operator:
                return True
        return False

    def isOperator(self, token):
        if token in self.operators:
            return True
        return False

    def isSeparator(self, token):
        if token in self.separators:
            return True

    def tokenizeLine(self, line: str):
        token = ''
        index = 0
        while index < len(line):
            if line[index] == " " or line[index] == "" or line[index] is None or line[index] == "\n":
                token = line[index]
                self.tokens.append(token)
            elif self.isSeparator(line[index]):
                token = line[index]
                self.tokens.append(token)
                token = ''
            elif self.isPartOfOperator(line[index]):
                token = line[index]
                if index < len(line) - 1:
                    if self.isPartOfOperator(line[index + 1]):
                        token += line[index + 1]
                        index += 1
                    if self.isOperator(token):
                        self.tokens.append(token)
                        token = ''
                    else:
                        return token
            else:
                token = line[index]
                if index < len(line) - 1 and not self.isSeparator(line[index + 1]):
                    index2 = index + 1
                    while index2 < len(line) and not self.isSeparator(line[index2]):
                        token += line[index2]
                        index2 += 1
                    index = index2
                if token in self.tokens:
                    pass
                elif self.isReservedWord(token):
                    self.tokens.append(token)
                elif self.isIdentifier(token):
                    self.tokens.append(token)
                elif self.isConstant(token):
                    self.tokens.append(token)
                elif self.isStringConstant(token):
                    self.tokens.append(token)
                else:
                    return token
            index += 1
        return None
