"""
    Classe définissant un état
"""
class State :

    def __init__(self, name):
        self.name = name

    def printState(self):
        print("Etat {op1}".format(op1 = self.name))

    def getStateName(self):
        return self.name