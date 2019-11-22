#Compte le nombre de caracteres, moyenne et ecart type pour les fichiers d un repertoire
#Passer en parametres :
#  param 1 : chemin vers le repertoire contenant les fichiers de reference (cleans)
#  param 2 : chemin vers le repertoire qui contenant les fichiers a analyser (BS,JT...)

import os
from math import pow
import math 
import sys

repClean = ""
repOutput = ""

if len(sys.argv)==3:
    repClean = sys.argv[1] #contient chemin du repertoire contenant les fichiers clean
    repOutput = sys.argv[2] #contient chemin du repertoire contenant les fichiers generes (BS,JT...)

if repOutput and repClean:

    #remplacement des / en \
    repClean = repClean.replace("/","\\")
    repOutput = repOutput.replace("/","\\")

    def countCarac(directory):
        nbCarac = 0
        ecartTypeCarac = 0
        nbFichier = 0
        listeCarac = []
        moyenneCarac = 0
        tempCarac = 0

        #parcours du repertoire
        for filename in os.listdir(directory):
            nbFichier = nbFichier +1
            tempCarac = 0
            try:
                content = open(directory+"\\"+filename,"r",encoding="utf8").read()      
                for paragraph in content: #parcours de chaque caracteres du fichier
                    nbCarac = nbCarac +1 #increment du nb de caracteres du repertoire
                    tempCarac = tempCarac +1 #variable temporaire pour nb de carac du fichier
                listeCarac.append(tempCarac)
                        
            except UnicodeDecodeError:
                print("file not utf8 : "+filename)


        moyenneCarac = nbCarac/nbFichier #calcul moyenne nb de caracteres par fichier

        #calcul de l ecart type
        for value in listeCarac:
            ecartTypeCarac = ecartTypeCarac + pow(value-moyenneCarac,2)

        ecartTypeCarac = ecartTypeCarac * (1/(nbFichier-1))
        ecartTypeCarac = math.sqrt(ecartTypeCarac)

        
        print("nbCaracs : {0}".format(nbCarac))
        print("MoyenneCarac : {0}".format(moyenneCarac))
        print("EcartTypeCaracs : {0}".format(ecartTypeCarac))
        
        
        
    print("-----infos Carac clean-----")
    countCarac(repClean)
    print("----------------------------")
    print("-----infos Carac "+repOutput+"-----")
    countCarac(repOutput)
    print("-------------------------")

else:
    print("missing parameters : repertoire fichiers clean et repertoire fichiers (BS,JT...)")