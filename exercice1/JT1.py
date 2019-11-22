#Extraction de donnees web a partir de l outil JUSTEXT
#Passer en parametres :
#  param 1 : chemin vers le repertoire contenant les fichiers html bruts
#  param 2 : chemin vers le repertoire qui contiendra les fichiers de sortie

import justext
import os
import re
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
        try:
            content = open(repHtml+"\\"+filename,"r",encoding="utf8").read()
            paragraphs = justext.justext(content,justext.get_stoplist("English")) #stoplist english par defaut car oblige de mettre une langue
            f = open(repOutput+"\\"+filename, "w",encoding="utf8")        
            for paragraph in paragraphs: #lecture des paragraphes du fichier
                if not paragraph.is_boilerplate:   
                    f.write("<"+paragraph.dom_path.rsplit('.', 1)[-1]+">"+paragraph.text+"<"+paragraph.dom_path.rsplit('.', 1)[-1]+">\n") #ajout du nom des balises paragraphe
                    
        except UnicodeDecodeError:
            print("file not utf8 : "+filename)
else:
    print("missing parameters : repertoire fichiers HTML et repertoire de sortie")

