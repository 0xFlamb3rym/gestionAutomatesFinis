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
        print(" Automate avec {op1} états et {op2} "
              "transitions".format(op1 = len(self.states),
              op2 = len(self.transitions)))

        print ("alphabet: {op1}".format(op1 = self.alphabet))
        for i in range(len(self.states)):
            self.states[i].printState()

        print ("Initial : {op1}".format(op1 = self.initialStates))
        print ("Finals : {op1}".format(op1 = self.finalStates))

        for i in range(len(self.transitions)):
            self.transitions[i].printTransition()
