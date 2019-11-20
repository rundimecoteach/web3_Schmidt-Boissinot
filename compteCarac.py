import os
from math import pow
import math 


def countCarac(directory):
    nbCarac = 0
    ecartTypeCarac = 0
    nbFichier = 0
    listeCarac = []
    moyenneCarac = 0
    tempCarac = 0

    for filename in os.listdir(directory):
        nbFichier = nbFichier +1
        tempCarac = 0
        try:
            content = open(directory+"\\"+filename,"r",encoding="utf8").read()      
            for paragraph in content:
                nbCarac = nbCarac +1
                tempCarac = tempCarac +1
            listeCarac.append(tempCarac)
                    
        except UnicodeDecodeError:
            print("file not utf8 : "+filename)


    moyenneCarac = nbCarac/nbFichier

    for value in listeCarac:
        ecartTypeCarac = ecartTypeCarac + pow(value-moyenneCarac,2)

    ecartTypeCarac = ecartTypeCarac * (1/(nbFichier-1))
    ecartTypeCarac = math.sqrt(ecartTypeCarac)

    
    print("nbCaracs : {0}".format(nbCarac))
    print("MoyenneCarac : {0}".format(moyenneCarac))
    print("EcartTypeCaracs : {0}".format(ecartTypeCarac))
    
    
    
print("-----infos Carac clean-----")
countCarac("D:\Documents\Master2\Web3.0\lejeune\Corpus_detourage\clean")
print("----------------------------")
print("-----infos Carac JT-----")
countCarac("D:\Documents\Master2\Web3.0\lejeune\JT")
print("-------------------------")