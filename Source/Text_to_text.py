from csv import reader
from fnmatch import translate
import googletrans 
from googletrans import Translator
import Text_To_Text
from OneDriveapi.Files_to_OneDrive import uploadToOneDrive
import PyPDF2
import os
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


def inputToText():
    if (exists("../OutputFiles/TranslatedText.txt")):
        os.remove("../OutputFiles/TranslatedText.txt")
    t = Text_To_Text.TxtToTxt()
    print("")
    text = input("Enter your text in: ") #Can the user type in spaces, try to see if it works
    print("")
    language_to_trans = input("Enter in the language that you want the text to be translated to: ") #Somehow need to ensure valid language entered
    print("")
    t.translateText(text, "../OutputFiles/TranslatedText.txt", language_to_trans) #Now translate it and output to file
    translator = Translator()
    translated_text = translator.translate(text,src = translator.detect(text).lang, dest = language_to_trans)
    print("Here is your translated text: " + translated_text.text)
    print("")
    input_upload = input("Do you want to save this file to OneDrive? y - Yes, n - No ")
    print("")
    if (input_upload == "y"):
        print("You will be redirected to sign in to Microsoft OneDrive.\n" + 
        "Type the generated code and follow the instructions.\n" + "This is a one-time procedure.\n" + 
        "If you already signed in to OneDrive. Type y.\n")
        response = input("Proceed?\n y - Yes, n - No: ")
        print("")
        if (response == "y"):
            uploadToOneDrive("../OutputFiles/TranslatedText.txt")
            print("Successfully uploaded file!")

def fileToText():
    if (exists("../OutputFiles/TranslatedFile.txt")):
        os.remove("../OutputFiles/TranslatedFile.txt")
    t = Text_To_Text.TxtToTxt()
    file_to_trans = input("Type in the name of the file that you want to be translated: ")
    print("")
    language_to_trans = input("Enter in the language that you want the text to be translated to: ")
    print("")
    t.translateFile(file_to_trans, "../OutputFiles/TranslatedFile.txt", language_to_trans) #why underlined, we defined translateFile in TextTest.py
    input_upload = input("Do you want to save this file to OneDrive? y - Yes, n - No ")
    print("")
    if (input_upload == "y"):
        print("You will be redirected to sign in to Microsoft OneDrive.\n" + 
        "Type the generated code and follow the instructions.\n" + "This is a one-time procedure.\n" + 
        "If you already signed in to OneDrive. Type y.\n")
        response = input("Proceed?\n y - Yes, n - No: ")
        print("")
        if (response == "y"):
            uploadToOneDrive("../OutputFiles/TranslatedFile.txt")
            print("Successfully uploaded file!")