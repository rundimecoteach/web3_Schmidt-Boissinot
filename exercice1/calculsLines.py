#Compte le nombre de lignes, moyenne et ecart type pour les fichiers d un repertoire
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


    def countLine(directory):
        nbLigne = 0
        ecartTypeLigne = 0
        nbFichier = 0
        listeLigne = [];
        moyenneLigne = 0

        #parcours du repertoire
        for filename in os.listdir(directory):
            nbFichier = nbFichier +1 #increment du nb total de fichiers
            try:
               nbLigne = nbLigne + len(open(directory+"\\"+filename,"r",encoding="utf8").readlines()) #increment du nb total de lignes
               listeLigne.append(len(open(directory+"\\"+filename,"r",encoding="utf8").readlines())) #liste du nb de lignes par fichier (pour calcul ecart type)
                        
            except UnicodeDecodeError:
                print("file not utf8 : "+filename)


        moyenneLigne = nbLigne/nbFichier #moyenne nb de lignes par fichier

        #calcul de l ecart type
        for value in listeLigne:
            ecartTypeLigne = ecartTypeLigne + pow(value-moyenneLigne,2)

        ecartTypeLigne = ecartTypeLigne * (1/(nbFichier-1))
        ecartTypeLigne = math.sqrt(ecartTypeLigne)

        
        print("nbLignes : {0}".format(nbLigne))
        print("MoyenneLigne : {0}".format(moyenneLigne))
        print("EcartTypeLignes : {0}".format(ecartTypeLigne))
        
        
        
    print("-----infos lignes clean-----")
    countLine(repClean)
    print("----------------------------")
    print("-----infos lignes "+repOutput+"-----")
    countLine(repOutput)
    print("-------------------------")

else:
    print("missing parameters : repertoire fichiers clean et repertoire fichiers (BS,JT...)")