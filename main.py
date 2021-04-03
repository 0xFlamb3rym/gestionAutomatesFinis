from automatlib.runAutomat import *
import sys

mode = ['0', '1', '2']

if __name__ == "__main__":

    if len(sys.argv)<4:
        print("Pas assez d'arguments en parametres\n")
        exit()

    if sys.argv[1] not in mode  :  #Prise en charge des AFN
            runAFN(sys.argv[1], sys.argv[2], sys.argv[3])

    else :
        if sys.argv[1] in mode:
            if sys.argv[1] == mode[0]:     #Prise en charge des AFD
                runAFD (sys.argv[2], sys.argv[3], sys.argv[4])
            if sys.argv[1] == mode[1]:     #Minimisation d'un AFD
                runMinimization(sys.argv[2], sys.argv[3])