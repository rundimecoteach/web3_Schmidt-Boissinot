import json
import justext
import os

langue = ""

dir = "C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\html"

with open('C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\doc_lg.json') as json_file:
    data = json.load(json_file)
    for filename in data:
        try:
            langue = data[filename]
            print(filename+" : "+langue)
            if langue == "Chinese":
            	langue = "English"
            file = open(dir+"\\"+filename,"r",encoding="utf8").read()
            paragraphs = justext.justext(file,justext.get_stoplist(langue))
            f = open("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\JT_trueLg\\"+filename, "w",encoding="utf8")        
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:   
                    f.write("<"+paragraph.dom_path.rsplit('.', 1)[-1]+">"+paragraph.text+"<"+paragraph.dom_path.rsplit('.', 1)[-1]+">\n")               
        except UnicodeDecodeError:
            print("file not utf8 : "+filename)
        except FileNotFoundError:
        	print("file not found : "+filename)