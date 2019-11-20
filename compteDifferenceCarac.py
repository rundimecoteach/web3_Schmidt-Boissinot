import os
from math import pow
import math 


nbCarac = 0
ecartTypeCarac = 0
nbFichier = 0
listeCarac = []
moyenneCarac = 0

tempCarac = 0
tempCaracClean = 0

for filename in os.listdir("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web_3.0\\TP_WEB_SCRAPPING\\JT"):
    for filenameClean in os.listdir("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web_3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\clean"):
        if filename == filenameClean :
            nbFichier = nbFichier +1
            tempCarac = 0
            tempCaracClean = 0
            try:
                content = open("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web_3.0\\TP_WEB_SCRAPPING\\JT\\"+filename,"r",encoding="utf8").read()      
                for paragraph in content:
                    tempCarac = tempCarac +1
                    
                contentClean = open("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web_3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\clean\\"+filename,"r",encoding="utf8").read()      
                for paragraph in contentClean:
                    tempCaracClean = tempCaracClean +1    
                
                nbCarac = nbCarac + abs(tempCarac-tempCaracClean)
                listeCarac.append(abs(tempCarac-tempCaracClean))
                
            except UnicodeDecodeError:
                print("file not utf8 : "+filename)             
    


moyenneCarac = nbCarac/nbFichier

for value in listeCarac:
    ecartTypeCarac = ecartTypeCarac + pow(value-moyenneCarac,2)

ecartTypeCarac = ecartTypeCarac * (1/(nbFichier-1))
ecartTypeCarac = math.sqrt(ecartTypeCarac)

print("-----infos différence carac JT-----")
print("nbDiff : {0}".format(nbCarac))
print("MoyenneDiff : {0}".format(moyenneCarac))
print("EcartTypeDiff : {0}".format(ecartTypeCarac))
print("--------------------------------")
    