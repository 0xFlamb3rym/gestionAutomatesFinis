from automatlib.state import *
from automatlib.transition import *
import sys

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

        """"@TODO"""

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

    def searchDStStates(self, srcState, symbol):
        if self.validSymbol(symbol) == 0:
            print("Le symbol n'est pas valide !!\r\n")
            return None

        res = []
        if self.validState(int(srcState)) == 0:
            print("L'etat n'est pas valide !!\r\n")
            return None

        for i in range(len(self.transitions)):
            if (str(srcState) == self.transitions[i].stateFrom) and (symbol == self.transitions[i].label):
                res.append(self.transitions[i].getStateTo())

        if len(res) > 0:
            return res

        return srcState

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

    def validWordAFN(self, word):
        """Dans le cas d'un AFN verifie si le mot est accepté ou pas
                @:return 1 si le mot est accepté sinon 0"""
        currentState = []
        nextState = []

        for sState in self.initialStates:
            currentState.append(sState)

        for w in word:
            for current in currentState:
                nextState += self.searchDStStates(current, w)

            nextState = list(set(nextState))
            currentState = nextState.copy()
            nextState.clear()

        for current in currentState:
            if current in self.finalStates:
                return 1

        return 0

    def minimization(self, exitFileName):
        Classe = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']

        initialisation = []
        initialisation1 = []
        equal = 0
        sState = []
        tmpState = []
        for i in range(len(self.states)):
            if str(self.states[i].name) in self.finalStates:
                initialisation.append(Classe[1])
            else:
                initialisation.append(Classe[0])

        while equal != len(initialisation):
            sState.clear()
            tmpState.clear()

            for i in range ( len ( self.states ) ) :
                for symbol in self.alphabet :
                    tmpState.append ( self.searchDstState ( str ( self.states[i].name ), symbol ) )
                sState.append ( tmpState.copy () )
                tmpState.clear ()

            for i in range (len(sState)):
                for j in range(len(sState[i])):
                    sState[i][j] = initialisation[int(sState[i][j])]

            classeValue = 0
            for i in range(len(sState)):
                if sState[i] in tmpState:
                    var = tmpState.index(sState[i])
                    initialisation1.append(Classe[var])
                else:
                    tmpState.append(sState[i])
                    initialisation1.append(Classe[classeValue])
                    classeValue = classeValue + 1

            equal = 0
            for i in range(len(initialisation)):
                if initialisation[i] == initialisation1[i]:
                    equal = equal + 1
            initialisation = initialisation1.copy()
            initialisation1.clear()
        tmpState.clear()
        newInitialisation = []
        for i in range(len(initialisation)):
            tmpState.append ( initialisation[i] )
            for j in range(len(self.alphabet)):
                tmpState.append(sState[i][j])
            newInitialisation.append(tmpState.copy())
            tmpState.clear()

        nNewInitialisation = []
        stateName = []
        for i in range(len(initialisation)):
            if newInitialisation[i] not in nNewInitialisation:
                nNewInitialisation.append(newInitialisation[i])
                stateName.append(i)

        nbStates = len(nNewInitialisation)
        newInitialStates = []
        newFinalStates = []
        for i in range(len(stateName)):
            if str(stateName[i]) in self.initialStates:
                newInitialStates.append(i)
            if str(stateName[i]) in self.finalStates:
                newFinalStates.append(i)

        try :
            file = open(exitFileName, "a")
        except :
            sys.exit("Fichier introuvable !!!")
        for symbol in self.alphabet:
            file.write("{opt1}".format(opt1 = symbol))
        file.write("\n")
        file.write("{opt1}".format(opt1 = nbStates))
        for i in newInitialStates:
            file.write ( "{opt1} ".format ( opt1 = i ) )
        file.write ( "\n")
        for i in newFinalStates:
            file.write ( "{opt1} ".format ( opt1 = i ) )
        file.write ( "\n")

        file.close ()
        """
            A terminer !!!!!
        """




    """
    @TO DO
    addTransitions
    """