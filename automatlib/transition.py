"""
    Classe définissant une transition
"""
class Transition :

    def __init__(self, stateFrom, stateTo, label):
        self.stateFrom = stateFrom
        self.stateTo = stateTo
        self.label = label

    def printTransition(self):
        print("{op1} --> {op2} étiquette: {op3}".format(op1 = self.stateFrom,
              op2 = self.stateTo, op3 = self.label))

    def getStateFrom(self):
        return self.stateFrom

    def getStateTo(self):
        return self.stateTo

    def getLabel(self):
        return self.label
