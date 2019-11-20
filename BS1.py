from bs4 import BeautifulSoup
import os
import math

dir = "C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\html"

for filename in os.listdir(dir):
    print(filename)
    try:
        file = open(dir+"\\"+filename,"r", encoding="utf8") 
        soup = BeautifulSoup(file.read(), 'html.parser')

        #on enleve le contenu des balises script contenant du code js
        for script in soup.find_all('script', src=False):
            script.decompose()

        #creation du fichier de sortie
        output = open("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\BS\\"+filename,"w",encoding="utf8")
        for i in soup.find_all(recursive = False):
    	    #on enleve les lignes vides
            items = ' '.join(i.text.split())
            if items != '' :      	
                output.write("\n<p>"+items+"</p>") #ajout de balises p pour marquer les paragraphes
        
    except UnicodeDecodeError:
        print("file not utf8 : "+filename) #certains fichiers n ont pas le bon encodage