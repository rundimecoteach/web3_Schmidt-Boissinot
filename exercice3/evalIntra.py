#Evaluation intraseque par langue et pour toutes les langues (fmesure, rappel, precision)
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


if repOutput and repClean and repJson:

    #remplacement des / en \
    repClean = repClean.replace("/","\\")
    repOutput = repOutput.replace("/","\\")
    repJson = repJson.replace("/","\\")

    #nom fichier de sortie
    split = repOutput.split("\\")
    fileNameOutput = split[len(split)-1]

    dir = ""
    langue = ""
    calculs = {}
    calculs["allF"] = 0
    calculs["allR"] = 0
    calculs["allP"] = 0
    calculs["nball"] = 0
    calculs["elF"] = 0
    calculs["elR"] = 0
    calculs["elP"] = 0
    calculs["nbel"] = 0
    calculs["enF"] = 0
    calculs["enR"] = 0
    calculs["enP"] = 0
    calculs["nben"] = 0
    calculs["plF"] = 0
    calculs["plR"] = 0
    calculs["plP"] = 0
    calculs["nbpl"] = 0
    calculs["ruF"] = 0
    calculs["ruR"] = 0
    calculs["ruP"] = 0
    calculs["nbru"] = 0
    calculs["zhF"] = 0
    calculs["zhR"] = 0
    calculs["zhP"] = 0
    calculs["nbzh"] = 0   

    #parcours du fichier JSON des langues
    with open(repJson) as json_file:
        data = json.load(json_file)
        for filename in data: #parcours de chaque fichier trouve dans le JSON
            langue = data[filename] #extraction de la langue du fichier

            try:
                testExists = open(repOutput+"\\"+filename,"r",encoding="utf8").read() #teste si fichier existe (si non passe dans l exception)
                print(filename+" "+langue)
                result = evaluate(repOutput+"\\"+filename,repClean+"\\"+filename) #calculs fmesure, rappel, precision avec le fichier et sa reference

                #construction du tableau de resultats (all langues et par langues)

                calculs["allF"] = calculs["allF"]+result["f-score"]
                calculs["allR"] = calculs["allR"]+result["recall"]
                calculs["allP"] = calculs["allP"]+result["precision"]
                calculs["nball"] = calculs["nball"]+1
                if langue == "Greek":
                    calculs["elF"] = calculs["elF"]+result["f-score"]
                    calculs["elR"] = calculs["elR"]+result["recall"]
                    calculs["elP"] = calculs["elP"]+result["precision"]
                    calculs["nbel"] = calculs["nbel"]+1
                elif langue=="English":
                    calculs["enF"] = calculs["enF"]+result["f-score"]
                    calculs["enR"] = calculs["enR"]+result["recall"]
                    calculs["enP"] = calculs["enP"]+result["precision"]
                    calculs["nben"] = calculs["nben"]+1
                elif langue=="Polish":
                    calculs["plF"] = calculs["plF"]+result["f-score"]
                    calculs["plR"] = calculs["plR"]+result["recall"]
                    calculs["plP"] = calculs["plP"]+result["precision"]
                    calculs["nbpl"] = calculs["nbpl"]+1
                elif langue=="Russian":
                    calculs["ruF"] = calculs["ruF"]+result["f-score"]
                    calculs["ruR"] = calculs["ruR"]+result["recall"]
                    calculs["ruP"] = calculs["ruP"]+result["precision"]
                    calculs["nbru"] = calculs["nbru"]+1
                elif langue=="Chinese":
                    calculs["zhF"] = calculs["zhF"]+result["f-score"]
                    calculs["zhR"] = calculs["zhR"]+result["recall"]
                    calculs["zhP"] = calculs["zhP"]+result["precision"]
                    calculs["nbzh"] = calculs["nbzh"]+1   
            except FileNotFoundError:
                print("file not found : "+filename)

    #calcul des moyennes pour les valeurs trouvees

    data={}
    data["all"]=[]
    data["all"].append({
        "allF":(calculs["allF"]/calculs["nball"]),
        "allR" :(calculs["allR"]/calculs["nball"]),
        "allP":(calculs["allP"]/calculs["nball"])
        })

    data["el"]=[]
    data["el"].append({
        "elF":(calculs["elF"]/calculs["nbel"]),
        "elR" :(calculs["elR"]/calculs["nbel"]),
        "elP":(calculs["elP"]/calculs["nbel"])
        })

    data["en"]=[]
    data["en"].append({
        "enF":(calculs["enF"]/calculs["nben"]),
        "enR" :(calculs["enR"]/calculs["nben"]),
        "enP":(calculs["enP"]/calculs["nben"])
        })

    data["pl"]=[]
    data["pl"].append({
        "plF":(calculs["plF"]/calculs["nbpl"]),
        "plR" :(calculs["plR"]/calculs["nbpl"]),
        "plP":(calculs["plP"]/calculs["nbpl"])
        })

    data["ru"]=[]
    data["ru"].append({
        "ruF":(calculs["ruF"]/calculs["nbru"]),
        "ruR" :(calculs["ruR"]/calculs["nbru"]),
        "ruP":(calculs["ruP"]/calculs["nbru"])
        })

    data["zh"]=[]
    data["zh"].append({
        "zhF":(calculs["zhF"]/calculs["nbzh"]),
        "zhR" :(calculs["zhR"]/calculs["nbzh"]),
        "zhP":(calculs["zhP"]/calculs["nbzh"])
        })

    #sauvegarde des resultats dans un nouveau fichier JSON
    with open("resFile"+fileNameOutput+".json","w") as resCalculs:
        json.dump(data,resCalculs)

else:
    print("missing parameters : repertoire fichiers clean,repertoire fichiers (BS,JT...),repertoire avec json contenant les bonnes langues")