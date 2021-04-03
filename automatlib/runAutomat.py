from automatlib.mapping import *

def runAFD(automatFileName, words_FileName, exitFileName):
    aAutomat = initAutomat(automatFileName)
    words = loadWordsFromFile(words_FileName)

    res = []
    for w in words:
        res.append(aAutomat.validWordAFD(w))

    writeFile(res, exitFileName)

def runAFN(automatFileName, words_FileName, exitFileName):
    aAutomat = initAutomat ( automatFileName )
    words = loadWordsFromFile ( words_FileName )

    res = []
    for w in words :
        res.append ( aAutomat.validWordAFN ( w ) )

    writeFile ( res, exitFileName )

def runMinimization(automatFileName, exitFileName):
    aAutomat = initAutomat (automatFileName)
    aAutomat.minimization(exitFileName)
