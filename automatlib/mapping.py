import sys

from automatlib.automat import *

"""
    Cette fonction permet de lire un fichier
    et retire les retours à la ligne
"""
def readFile(fileName):
    try:
        file = open(fileName, "r")
    except:
        sys.exit ("Fichier introuvable !!!")

    file_data = []
    for line in file:
        file_data.append(line.rstrip("\n"))

    file.close()

    return file_data

"""
    Cette fonction permet d'ecrire dans un fichier
"""
def writeFile(fileData, fileName):
    try :
        file = open(fileName, "a")
    except :
        sys.exit("Fichier introuvable !!!")

    for data in fileData:
        file.write("{op1}\n".format(op1 = data))

    file.close()

"""
    Initialisation de l'alphabet
"""
def initAlphabet(alphabet):

    return list(alphabet.strip())

"""
    Creation d'une liste d'etats
"""
def initStates(nbState):
    lstState = []
    for i in range(int(nbState)):
        lstState.append(State(i))
        # lstState[i].printState()

    return lstState

"""
    Creation d'une liste de mot
"""
def initLine(line):

    return list(line.split(" "))

"""
    Creation d'une transition
"""
def initTransition(line):
    lst = initLine(line)
    transition = Transition(lst[0], lst[1], lst[2])

    return transition

"""
    Creation d'un automate
"""
def initAutomat(fileName):
    """lecture du fichier"""
    fileData = readFile(fileName)

    """initialisation de l'alphabet"""
    alphabet = initAlphabet(fileData[0])

    """Creation de la liste des états"""
    states = initStates(fileData[1])

    """Initialisation des états initiaux"""
    initialStates = initLine(fileData[2])

    """Initialisations des états acceptants"""
    finalStates = initLine(fileData[3])

    """Initialisations des transitions"""
    transitions = []
    for i in range(4, len(fileData)):
        transitions.append(initTransition(fileData[i]))

    """Creation de l'automate"""
    Automate = Automat( alphabet, states, initialStates,
                        finalStates, transitions )

    return Automate

"""
    chargement d'une liste de mots
"""
def loadWordsFromFile(fileName):
    fileData = readFile(fileName)

    return fileData

"""if __name__ == "__main__":
    file_Name = "../Instances/AFN/afn1.txt"
    wordsFileName = "../Instances/AFN/mots1.txt"""""

