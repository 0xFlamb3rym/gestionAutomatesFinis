from automatlib.state import *
from automatlib.transition import *

"""
    Classe définissant un automate
"""
class Automat :

    def __init__(self, p_alphabet, p_states, p_initialStates,
                p_finalStates, p_transitions):
        self.alphabet = p_alphabet
        self.states = p_states
        self.initialStates = p_initialStates
        self.finalStates = p_finalStates
        self.transitions = p_transitions

    def printAutomat(self):
        """Affiche un automate"""
        print("Automate avec {op1} états et {op2} "
              "transitions".format(op1 = len(self.states),
              op2 = len(self.transitions)))

        print ("alphabet: {op1}".format(op1 = self.alphabet))
        for i in range(len(self.states)):
            self.states[i].printState()

        print ("Initial : {op1}".format(op1 = self.initialStates))
        print ("Finals : {op1}".format(op1 = self.finalStates))

        for i in range(len(self.transitions)):
            self.transitions[i].printTransition()

    def addTransitions(self, newTransition):
        """Ajoute une transition"""
        res = self.validState(newTransition.stateFrom)
        if res == 0:
            print ("L'etat source n'est pas valide !!!\r\n")
            return None

        res = self.validState(newTransition.stateTo)
        if res == 0 :
            print ("L'etat de destination n'est pas valide !!!\r\n")
            return None

        res = self.validSymbol(newTransition.label)
        if res == 0 :
            print ("Le label n'est pas valide !!!\r\n")
            return None


    def addStates(self, newState):
        """Ajoute un etat"""
        exist = self.validState(newState.name)
        if exist == 0:
            self.states.append(newState)
        else:
            print("Cet état existe deja!!")

    def validSymbol(self, symbol):
        """Verifie si le symbole est valide
        @:return 1 si le symbole est valide sinon 0 """
        if symbol not in self.alphabet:
            return 0

        return 1

    def validState(self, stateName):
        """verifie si l'état existe
        @:return 1 si l'état existe sinon 0"""
        if stateName < len(self.states):
            return 1

        return 0

    def addInitialState(self, stateName):
        """Ajoute un etat initial"""
        res = self.validState(stateName)
        if res == 1:
            if res not in self.initialStates:
                self.initialStates.append(stateName)
        if res == 0:
            print("Cet etat n'est pas valide !\r\n")

    def addFinalState(self, stateName):
        """Ajoute un etat final"""
        res = self.validState (stateName)
        if res == 1 :
            if res not in self.initialStates :
                self.finalStates.append (stateName)
        if res == 0 :
            print ("Cet etat n'est pas valide !\r\n")

    def searchDstState(self, srcState, symbol):
        if self.validState(int(srcState)) == 0:
            print("L'etat n'est pas valide !!\r\n")
            return None

        if self.validSymbol(symbol) == 0:
            print("Le symbol n'est pas valide !!\r\n")
            return None

        for i in range(len(self.transitions)):
            if (str(srcState) == self.transitions[i].stateFrom) and (symbol == self.transitions[i].label):
                return self.transitions[i].getStateTo()

    def validWordAFD(self, word):
        """Dans le cas d'un AFD verifie si le mot est accepté ou pas
        @:return 1 si le mot est accepté sinon 0"""
        currentState = self.initialStates[0]
        for w in word:
            """Verifie si le mot/symbole est est valide"""
            res = self.validSymbol(w)
            if res == 0:
                print("Le mot [{opt1}]n'est pas valide !!!".format(opt1 = word))
                return 0

            nextState = self.searchDstState(currentState, w)
            if nextState is None:
                return 0

            currentState = nextState

        if currentState in self.finalStates:
            return 1

        return 0



    """
    @TO DO
    addTransitions
    """