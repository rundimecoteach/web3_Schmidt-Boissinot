#Extraction de donnees avec JUSTEXT et integration de l outil LANGID pour reconnaissance de la langue
#Passer en parametres :
#  param 1 : chemin vers le repertoire contenant les fichiers html bruts
#  param 2 : chemin vers le repertoire qui contiendra les fichiers de sortie

import justext
import os
import langid
import sys


repHtml = ""
repOutput = ""

if len(sys.argv)==3:
    repHtml = sys.argv[1] #contient nom du repertoire contenant les fichiers a analyser
    repOutput = sys.argv[2] #repertoire de sortie

#correspondance des langues avec leur code ISO
langues = {}
langues["el"] = "Greek"
langues["en"] = "English"
langues["ru"] = "Russian"
langues["pl"] = "Polish"
langues["zh"] = "English" #pour chinois on met anglais car existe pas
langFile = ""

if repOutput and repHtml:

    #remplacement des / en \
    repHtml = repHtml.replace("/","\\")
    repOutput = repOutput.replace("/","\\")

    for filename in os.listdir(repHtml):
        try:
            file = open(repHtml+"\\"+filename,"r",encoding="utf8").read()
            lang = langid.classify(file) #detection de la langue avec LANGID
            langFile = langues[lang[0]] #correspondance avec code ISO de la langue
            if langFile :
                print(filename+" "+langFile)
                paragraphs = justext.justext(file,justext.get_stoplist(langFile))
                f = open(repOutput+"\\"+filename, "w",encoding="utf8")        
                for paragraph in paragraphs:
                    if not paragraph.is_boilerplate:   
                        f.write("<"+paragraph.dom_path.rsplit('.', 1)[-1]+">"+paragraph.text+"<"+paragraph.dom_path.rsplit('.', 1)[-1]+">\n") #ajout du nom des balises paragraphe
        except UnicodeDecodeError:
            print("file not utf8 : "+filename)

else:
    print("missing parameters : repertoire fichiers HTML et repertoire de sortie")