#Calcule la moyenne et l ecart-type de la difference de taille en caracteres par rapport au fichier de reference
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


nbCarac = 0
ecartTypeCarac = 0
nbFichier = 0
listeCarac = []
moyenneCarac = 0

tempCarac = 0
tempCaracClean = 0

if repOutput and repClean:

    #remplacement des / en \
    repClean = repClean.replace("/","\\")
    repOutput = repOutput.replace("/","\\")


    #parcours du repertoire de fichiers a comparer
    for filename in os.listdir(repOutput):
        #parcours des fichiers de reference
        for filenameClean in os.listdir(repClean):
            if filename == filenameClean :
                nbFichier = nbFichier +1 #nb total de fichiers
                tempCarac = 0
                tempCaracClean = 0
                try:
                    content = open(repOutput+"\\"+filename,"r",encoding="utf8").read()      
                    for paragraph in content: #parcours des caracteres du fichier
                        tempCarac = tempCarac +1
                        
                    contentClean = open(repClean+"\\"+filename,"r",encoding="utf8").read()      
                    for paragraph in contentClean: #parcours des caracteres du fichier clean
                        tempCaracClean = tempCaracClean +1    
                    
                    nbCarac = nbCarac + abs(tempCarac-tempCaracClean) #somme des differences (en caracteres)
                    listeCarac.append(abs(tempCarac-tempCaracClean)) #difference (en caracteres) pour chaque fichier
                    
                except UnicodeDecodeError:
                    print("file not utf8 : "+filename)             
        


    moyenneCarac = nbCarac/nbFichier #moyenne des differences

    #calcul de l ecart type des differences
    for value in listeCarac:
        ecartTypeCarac = ecartTypeCarac + pow(value-moyenneCarac,2)

    ecartTypeCarac = ecartTypeCarac * (1/(nbFichier-1))
    ecartTypeCarac = math.sqrt(ecartTypeCarac)

    print("-----infos différence carac "+repOutput+"-----")
    print("nbDiff : {0}".format(nbCarac))
    print("MoyenneDiff : {0}".format(moyenneCarac))
    print("EcartTypeDiff : {0}".format(ecartTypeCarac))
    print("--------------------------------")
    
else:
    print("missing parameters : repertoire fichiers clean et repertoire fichiers (BS,JT...)")