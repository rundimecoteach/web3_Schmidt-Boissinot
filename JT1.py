import justext
import os
import re

dir = "C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\html"
for filename in os.listdir(dir):
    try:
        content = open(dir+"\\"+filename,"r",encoding="utf8").read()
        paragraphs = justext.justext(content,justext.get_stoplist("English"))
        f = open("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\JT\\"+filename, "w",encoding="utf8")        
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:   
                f.write("<"+paragraph.dom_path.rsplit('.', 1)[-1]+">"+paragraph.text+"<"+paragraph.dom_path.rsplit('.', 1)[-1]+">\n") #ajout du nom des balises paragraphe
                
    except UnicodeDecodeError:
        print("file not utf8 : "+filename)

