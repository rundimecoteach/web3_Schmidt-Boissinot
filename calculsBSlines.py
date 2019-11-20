import os
from math import pow
import math 


def countLine(directory):
    nbLigne = 0
    ecartTypeLigne = 0
    nbFichier = 0
    listeLigne = [];
    moyenneLigne = 0

    for filename in os.listdir(directory):
        nbFichier = nbFichier +1
        try:
           nbLigne = nbLigne + len(open(directory+"\\"+filename,"r",encoding="utf8").readlines())
           listeLigne.append(len(open(directory+"\\"+filename,"r",encoding="utf8").readlines()))
                    
        except UnicodeDecodeError:
            print("file not utf8 : "+filename)


    moyenneLigne = nbLigne/nbFichier

    for value in listeLigne:
        ecartTypeLigne = ecartTypeLigne + pow(value-moyenneLigne,2)

    ecartTypeLigne = ecartTypeLigne * (1/(nbFichier-1))
    ecartTypeLigne = math.sqrt(ecartTypeLigne)

    
    print("nbLignes : {0}".format(nbLigne))
    print("MoyenneLigne : {0}".format(moyenneLigne))
    print("EcartTypeLignes : {0}".format(ecartTypeLigne))
    
    
    
print("-----infos lignes clean-----")
countLine("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web_3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\clean")
print("----------------------------")
print("-----infos lignes BS-----")
countLine("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web_3.0\\TP_WEB_SCRAPPING\\BS")
print("-------------------------")