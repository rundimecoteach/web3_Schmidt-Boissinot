#Evaluation intraseque par source et par langue (fmesure, rappel, precision)
#Passer en parametres :
#  param 1 : chemin vers le repertoire contenant les fichiers de reference (clean)
#  param 2 : chemin vers le repertoire qui contiendra les fichiers a analyser (BS,JT...)
#  param 3 : chemin vers le fichier JSON de verite terrain pour les langues

import os
import json
import subprocess
from test_eval import *
import sys

repClean = ""
repOutput = ""
repJson = ""
fileNameOutput = ""

if len(sys.argv)==4:
    repClean = sys.argv[1] #contient chemin du repertoire contenant les fichiers clean
    repOutput = sys.argv[2] #contient chemin du repertoire contenant les fichiers generes (BS,JT...)
    repJson = sys.argv[3] #contient chemin du repertoire contenant le fichier json avec les bonnes langues

langue = ""
siteName = ""
langues = {}
langues["Greek"] = []
langues["English"] = []
langues["Polish"] = []
langues["Russian"] = []
langues["Chinese"] = []
sites = {}

if repOutput and repClean and repJson:

    #remplacement des / en \
    repClean = repClean.replace("/","\\")
    repOutput = repOutput.replace("/","\\")
    repJson = repJson.replace("/","\\")

    #nom fichier de sortie
    split = repOutput.split("\\")
    fileNameOutput = split[len(split)-1]

    #parcours du fichier JSON des langues
    with open(repJson) as json_file:
        data = json.load(json_file)
        for filename in data: #parcours de chaque fichier trouve dans le JSON
            langue = data[filename] #extraction de la langue du fichier
            siteName = (filename.split("_"))[1] #nom du site (source)

            try:
                testExists = open(repOutput+"\\"+filename,"r",encoding="utf8").read()

                if siteName not in langues[langue]:
                    langues[langue].append(siteName) #association langues-sites

                if siteName not in sites:
                    values = {}
                    values["F"] = 0
                    values["R"] = 0
                    values["P"] = 0
                    values["nbPages"] = 0
                    sites[siteName]=[]
                    sites[siteName].append(values) #association sites-valeurs (initialisees a 0)

                result = evaluate(repOutput+"\\"+filename,repClean+"\\"+filename) #calculs fmesure, rappel, precision avec le fichier et sa reference
                #sauvegarde des resultats pour le site
                sites[siteName][0]['F'] = sites[siteName][0]['F']+result["f-score"]
                sites[siteName][0]['R'] = sites[siteName][0]['R']+result["recall"]
                sites[siteName][0]['P'] = sites[siteName][0]['P']+result["precision"]
                sites[siteName][0]['nbPages'] = sites[siteName][0]['nbPages']+1 #increment du nb de pages pour le site

            except FileNotFoundError:
                print("file not found : "+filename)

    #construction des données pour les sauvegarder dans un fichier json
    data={}
    cpt = 0
    for langue in langues: #parcours des langues
        data[langue]=[]
        cpt = 0
        for siteName in langues[langue]: #parcours des sites pour une langue
            data[langue].append([siteName])
            data[langue][cpt].append({
                "F":(sites[siteName][0]['F']/sites[siteName][0]['nbPages']), #moyenne f-mesure
                "R" :(sites[siteName][0]['R']/sites[siteName][0]['nbPages']), #moyenne rappel
                "P":(sites[siteName][0]['P']/sites[siteName][0]['nbPages']) #moyenne precision
            })
            cpt = cpt+1

    #sauvegarde des resultats dans un nouveau fichier JSON
    with open("resFileSites"+fileNameOutput+".json","w") as resCalculs:
        json.dump(data,resCalculs)

else:
    print("missing parameters : repertoire fichiers clean,repertoire fichiers (BS,JT...),repertoire avec json contenant les bonnes langues")