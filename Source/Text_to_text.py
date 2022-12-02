from googletrans import Translator  
import googletrans 
from os.path import exists
class TxtToTxt:
    @staticmethod
    def translateText(toTranslate, fileTo, chosenLanguage):  #Here we have some text written in TextTest.py, and we want to take that text and translate it into a desired language and then output to file                                  
        translator = Translator()
        # FIX LANGUAGE TAGS
        givenLanguage = translator.detect(toTranslate)          # detects original language in object format, use .lang for langtag 
        # Converts Desired Language to LangTag
        chosenLanguage = chosenLanguage.lower()
        languageTo = "key doesn't exist"
        for key, value in googletrans.LANGUAGES.items():
            if chosenLanguage == value:
                languageTo = key
        
        translated1 = translator.translate(toTranslate, src = givenLanguage.lang, dest = languageTo)  # Creates translation object translating from src to dest
        if (exists("../OutputFiles/" + toTranslate)):
            file = open(fileTo, "w", encoding = "utf-16") 
        else:
            file = open(fileTo, "a", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
        file.write(translated1.text)                                        # Write text from translated object
        file.close()                                                        # Closes file
        # #let's read the contents of the file now
        # file = open(fileTo,"r", encoding = "utf-16")         # Opens translated file for reading
        # print(file.read())                                                  # Prints the text in the written file
        # file.close()    
    
    @staticmethod
    def translateFile(toTranslateFile, fileTo, chosenLanguage): #We have a file and want to go through each line translate the text and output it to a file
        #First loop toTranslateFile
        #Take each line and translate it 
        #Then output it to file
        txtTranslator = TxtToTxt()  
        with open(toTranslateFile, "r") as from_file:
            for line in from_file:
                stripped_line = line.strip()
                txtTranslator.translateText(stripped_line, fileTo, chosenLanguage)
                file = open(fileTo, "a", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
                file.write('\n')                                        # Write text from translated object
                file.close()
        file = open(fileTo,"r", encoding = "utf-16")                         # Opens translated file for reading
        print(file.read())                                                  # Prints the text in the written file
        file.close()   
        print("")
 
 #WORKS
# def translateText(toTranslate, fileTo, chosenLanguage):  #Here we have some text written in TextTest.py, and we want to take that text and translate it into a desired language and then output to file                                  
#     translator = Translator()
#     # FIX LANGUAGE TAGS
#     givenLanguage = translator.detect(toTranslate)          # detects original language in object format, use .lang for langtag 
#     # Converts Desired Language to LangTag
#     chosenLanguage = chosenLanguage.lower()
#     languageTo = "key doesn't exist"
#     for key, value in googletrans.LANGUAGES.items():
#         if chosenLanguage == value:
#             languageTo = key
#     translated1 = translator.translate(toTranslate, src = givenLanguage.lang, dest = languageTo)  # Creates translation object translating from src to dest
#     print(translated1.text)
#     if (exists("../Source/TranslatedText.txt")):
#         file = open(fileTo, "w", encoding = "utf-16") 
#     else:
#         file = open(fileTo, "a", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
#     file.write(translated1.text+"\n")                                        # Write text from translated object
#     file.close()                                                        # Closes file
#     # #let's read the contents of the file now
#     # file = open(fileTo,"r", encoding = "utf-16")         # Opens translated file for reading
#     # print(file.read())                                                  # Prints the text in the written file
#     # file.close()

##SEVERAL ISSUES
# def translateFile(toTranslateFile, fileTo, chosenLanguage): #We have a file and want to go through each line translate the text and output it to a file
#     #First loop toTranslateFile
#     #Take each line and translate it 
#     #Then output it to file
#     txtTranslator = Translator()  
#     with open("../Source/"+toTranslateFile, "r", encoding="utf-16") as from_file:
#     #print(file.read())
#     #print("at this point of the code")
#         for line in from_file:
#             stripped_line = line.strip()
#             #print(stripped_line)
#             translateText(stripped_line, fileTo, chosenLanguage)
#             # file = open(fileTo, "a", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
#             # file.write('\n')
#             # file.close()                                 # Write text from translated object
#         #from_file.close() 
##TAKE TWO
# def translateFile(toTranslateFile, fileTo, chosenLanguage): #We have a file and want to go through each line translate the text and output it to a file
#     #First loop toTranslateFile
#     #Take each line and translate it 
#     #Then output it to file
#     #txtTranslator = Translator()  
#     with open(toTranslateFile, "r", encoding = "utf-16") as from_file:
#         for line in from_file:
#             stripped_line = line.strip()
#             translateText(stripped_line, fileTo, chosenLanguage)
#             file = open(fileTo, "a", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
#             file.write('\n')                                        # Write text from translated object
#             file.close()
        