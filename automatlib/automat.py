from automatlib.state import State

"""
    Classe définissant un automate
"""
class Automat :

    def __int__(self, alphabet):
        self.alphabet = set(alphabet)
        self.state = ()
        self.initial_states = ()
        self.final_states = ()
        self.transitions = ()
