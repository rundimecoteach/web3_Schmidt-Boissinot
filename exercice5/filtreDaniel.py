#Permet de filtrer le fichier Daniel.json fournis pour l exercice 4
#Passer en parametres :
#  param 1 : chemin vers le repertoire qui contient les fichiers a analyser (BS,JT...)
#  param 2 : chemin vers le fichier Daniel.json a transformer
#  param 3 : chemin vers le repertoire qui contiendra le fichier json transforme

import json
import os
import sys

res = {}
rep = ""
repDaniel = ""
repDanielOutput = ""

if len(sys.argv)==4:   
    rep = sys.argv[1] #contient chemin du repertoire contenant les fichiers
    repDaniel = sys.argv[2] #contient chemin du repertoire contenant le daniel.json a transformer
    repDanielOutput = sys.argv[3] #repertoire de sortie pour le nouveau daniel.json

repName = ""

if rep and repDaniel and repDanielOutput:

    #remplacement des \ en /
    rep = rep.replace("\\","/")
    repDaniel = repDaniel.replace("\\","/")
    repDanielOutput = repDanielOutput.replace("\\","/")

    #recup nom du dossier contenant les fichiers a analyser
    split = rep.split("/")
    repName = split[len(split)-1]

    with open(repDaniel,'r',encoding="utf8") as json_file:
        data = json.load(json_file)
        for fileId in data:
            try:
                #test si fichier existe deja (si non passe dans l exception)
                f = open(rep+"/"+data[fileId]["path"], "r",encoding="utf8")

                #creation nouvel objet json (certains champs sont à renommer)
                res[fileId]={}
                res[fileId]["annotations"]={}
                res[fileId]["comment"]={}
                res[fileId]["date_collecte"]={}
                res[fileId]["language"]={}
                res[fileId]["document_path"]={}
                res[fileId]["url"]={}

                data[fileId]["path"] = repName+"/"+data[fileId]["path"] #ajout du path local pour le fichier

                res[fileId]["annotations"] = data[fileId]["annotations"]
                res[fileId]["comment"] = data[fileId]["comment"]
                res[fileId]["date_collecte"] = data[fileId]["date_collecte"]
                res[fileId]["language"] = data[fileId]["langue"]
                res[fileId]["document_path"] = data[fileId]["path"]
                res[fileId]["url"] = data[fileId]["url"]

            except FileNotFoundError:
                print("file not found : "+data[fileId]["path"])

    print(repName)
    newJson = open(repDanielOutput+"/"+"daniel"+repName+".json", "w",encoding="utf8")
    newJson.write(json.dumps(res))
else:
    print("Veuillez renseigner :  chemin du repertoire contenant les fichiers a analyser (doit etre au meme endroit que le fichier json),chemin pour le fichier daniel.json, chemin de sortie pour le nouveau daniel.json")