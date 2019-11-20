import justext
import os
import langid

langues = {}
langues["el"] = "Greek"
langues["en"] = "English"
langues["ru"] = "Russian"
langues["pl"] = "Polish"
langues["zh"] = "English" #pour chinois on met anglais car existe pas
langFile = ""

dir = "C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\Corpus_detourage\\Corpus_detourage\\html"
for filename in os.listdir(dir):
    try:
        file = open(dir+"\\"+filename,"r",encoding="utf8").read()
        lang = langid.classify(file) #detection de la langue
        langFile = langues[lang[0]]
        if langFile :
            print(filename+" "+langFile)
            paragraphs = justext.justext(file,justext.get_stoplist(langFile))
            f = open("C:\\Users\\Asus\\Documents\\Cours\\M2\\Web 3.0\\TP_WEB_SCRAPPING\\JT_langid\\"+filename, "w",encoding="utf8")        
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:   
                    f.write("<"+paragraph.dom_path.rsplit('.', 1)[-1]+">"+paragraph.text+"<"+paragraph.dom_path.rsplit('.', 1)[-1]+">\n")               
    except UnicodeDecodeError:
        print("file not utf8 : "+filename)