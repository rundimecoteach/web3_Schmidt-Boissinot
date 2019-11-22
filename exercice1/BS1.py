#Extraction de donnees web a partir de l outil BEAUTIFULSOUP
#Passer en parametres :
#  param 1 : chemin vers le repertoire contenant les fichiers html bruts
#  param 2 : chemin vers le repertoire qui contiendra les fichiers de sortie

from bs4 import BeautifulSoup
import os
import math
import sys

repHtml = ""
repOutput = ""

if len(sys.argv)==3:
    repHtml = sys.argv[1] #contient nom du repertoire contenant les fichiers a analyser
    repOutput = sys.argv[2] #repertoire de sortie


if repOutput and repHtml:

    #remplacement des / en \
    repHtml = repHtml.replace("/","\\")
    repOutput = repOutput.replace("/","\\")

    #parcours des fichiers html bruts
    for filename in os.listdir(repHtml):
        print(filename)
        try:
            file = open(repHtml+"\\"+filename,"r", encoding="utf8") 
            soup = BeautifulSoup(file.read(), 'html.parser') #creation objet BS avec contenu du fichier

            #on enleve le contenu des balises script contenant du code js
            for script in soup.find_all('script', src=False):
                script.decompose()

            #creation du fichier de sortie
            output = open(repOutput+"\\"+filename,"w",encoding="utf8")
            for i in soup.find_all(recursive = False):
        	    #on enleve les lignes vides
                items = ' '.join(i.text.split())
                if items != '' :      	
                    output.write("\n<p>"+items+"</p>") #ajout de balises p pour marquer les paragraphes
            
        except UnicodeDecodeError:
            print("file not utf8 : "+filename) #certains fichiers n ont pas le bon encodage

else:
    print("missing parameters : repertoire fichiers HTML et repertoire de sortie")
