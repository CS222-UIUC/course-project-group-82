from csv import reader
from fnmatch import translate
from googletrans import Translator
#from TextTest.OneLetter import translateText
#from Text_to_text import translateText, translateFile
import Text_To_Text
from OneDriveapi.Files_to_OneDrive import uploadToOneDrive
import PyPDF2
import os
from os.path import exists


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