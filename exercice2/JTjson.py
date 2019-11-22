#Extraction de donnees avec JUSTEXT et reconnaissance de la langue avec fichier JSON de verite terrain
#Passer en parametres :
#  param 1 : chemin vers le repertoire contenant les fichiers html bruts
#  param 2 : chemin vers le repertoire qui contiendra les fichiers de sortie
#  param 3 : chemin vers le fichier JSON de verite terrain pour les langues

import json
import justext
import os
import sys


repHtml = ""
repOutput = ""
repJson = ""

if len(sys.argv)==4:
    repHtml = sys.argv[1] #contient nom du repertoire contenant les fichiers a analyser
    repOutput = sys.argv[2] #repertoire de sortie
    repJson = sys.argv[3] #repertoire fichier json true lg

langue = ""

if repOutput and repHtml and repJson:

    repHtml = repHtml.replace("\\","/")
    repOutput = repOutput.replace("\\","/")
    repJson = repJson.replace("\\","/")

    #parcours du fichier JSON contenant les bonnes informations sur les langues
    with open(repJson) as json_file:
        data = json.load(json_file)
        for filename in data: #parcours de chaque fichiers trouves dans le JSON
            try:
                langue = data[filename] #extraction de la langue pour le fichier trouve
                print(filename+" : "+langue)
                if langue == "Chinese": #le chinois n est pas gere par justext
                	langue = "English"
                file = open(repHtml+"\\"+filename,"r",encoding="utf8").read()
                paragraphs = justext.justext(file,justext.get_stoplist(langue))
                f = open(repOutput+"\\"+filename, "w",encoding="utf8")        
                for paragraph in paragraphs:
                    if not paragraph.is_boilerplate:   
                        f.write("<"+paragraph.dom_path.rsplit('.', 1)[-1]+">"+paragraph.text+"<"+paragraph.dom_path.rsplit('.', 1)[-1]+">\n") #ajout du nom des balises paragraphe            
            except UnicodeDecodeError:
                print("file not utf8 : "+filename)
            except FileNotFoundError:
            	print("file not found : "+filename)

else:
    print("missing parameters : repertoire fichiers HTML, repertoire de sortie et repertoire du json avec les true languages")