class FiniteAutomata:

    def __init__(self):
        self.Q = [] # finite set of states
        self.E = [] # finite alphabet
        self.F = [] # set of final states
        self.q0 = [] # initial state
        self.D = [] # transition function
        self.readFromFile()

    def displayQ(self):
        return "set of states:\n" + self.Q.__str__()

    def displayE(self):
        return "alphabet:\n" + self.E.__str__()

    def displayD(self):
        return "transitions:\n" + self.D.__str__()

    def displayQ0(self):
        return "initial state:\n" + self.q0.__str__()

    def displayF(self):
        return "final states:\n" + self.D.__str__()

    def readFromFile(self):
        with open("FA.in", "r") as f:
            QLine = f.readline()
            ELine = f.readline()
            q0Line = f.readline()
            FLine = f.readline()
            DLine = f.readline()
            while True:
                line = f.readline()
                if not line:
                    break
                self.D.append(line[1:len(line)-1])
            # print(QLine)
            # print(ELine)
            # print(q0Line)
            # print(FLine)
            # print(DLine)

            for i in range(4, len(QLine), +2):
                self.Q.append(QLine[i])
            for i in range(4, len(ELine), +2):
                self.E.append(ELine[i])
            for i in range(5, len(q0Line), +2):
                self.q0.append(q0Line[i])
            for i in range(4, len(FLine), +2):
                self.F.append(FLine[i])
            # print(self.D)
