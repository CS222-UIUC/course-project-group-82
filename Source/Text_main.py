from csv import reader
from fnmatch import translate
from googletrans import Translator
#from TextTest.OneLetter import translateText
#from Text_to_text import translateText, translateFile
import Text_to_text
from OneDriveapi.Files_to_OneDrive import uploadToOneDrive
import PyPDF2

def inputToText():
    t = Text_to_text.TxtToTxt()
    text = input("Enter your text in: ") #Can the user type in spaces, try to see if it works
    print("")
    language_to_trans = input("Enter in the language that you want the text to be translated to: ") #Somehow need to ensure valid language entered
    print("")
    t.translateText(text, "../OutputFiles/TranslatedText.txt", language_to_trans) #Now translate it and output to file
    translator = Translator()
    translated_text = translator.translate(text,src = translator.detect(text).lang, dest = language_to_trans)
    print("Here is your translated text: " + translated_text.text)
    input_upload = input("Do you want to save this file to OneDrive? y - Yes, n - No ")
    if (input_upload == "y"):
        print("You will be redirected to sign in to Microsoft OneDrive.\n" + 
        "Type the generated code and follow the instructions.\n" + "This is a one-time procedure.\n")
        response = input("Proceed?\n y - Yes, n - No: ")
        if (response == "y"):
            uploadToOneDrive("../OutputFiles/TranslatedText.txt")
            print("Successfully uploaded file!")

def fileToText():
    t = Text_to_text.TxtToTxt()
    file_to_trans = input("Type in the name of the file that you want to be translated: ")
    language_to_trans = input("Enter in the language that you want the text to be translated to: ")
    t.translateFile(file_to_trans, "../OutputFiles/TranslatedFile.txt", language_to_trans) #why underlined, we defined translateFile in TextTest.py
    

#Archive Code
# #Here we want to create some sort of interface with the user such that the user can type words and get translated as well send in file
# intro = input("Hello There. Do you have anything you want to translate? y - Yes, n - No ")
# print("") #getting an error when try to get user input
# while (intro != "y" and intro != "n"):
#     intro = input("Do you have anything you want to translate? y - Yes, n - No ")
#     print("")
#     #print("Error!, enter y for yes or n for no")
# if (intro == "y"):
#     input_translate = input("Do you want to type anything or do you have a file that you want to be translated to?\nt - type, txt - translate text file: ")
#     print("")
#     while (input_translate != "t" and input_translate != "txt"):
#         input_translate = input("Do you want to type anything or do you have a file that you want to be translated to?\nt - type, txt - translate text file: ")
#         print("")
#     if (input_translate == "t"):
#         text = input("Enter your text in: ") #Can the user type in spaces, try to see if it works
#         print("")
#         language_to_trans = input("Enter in the language that you want the text to be translated to: ") #Somehow need to ensure valid language entered
#         print("")
#         translateText(text, "TranslatedText.txt", language_to_trans) #Now translate it and output to file
#         translator = Translator()
#         translated_text = translator.translate(text,src = translator.detect(text).lang, dest = language_to_trans)
#         print("Here is your translated text: " + translated_text.text)
#         input_upload = input("Do you want to save this file to OneDrive? y - Yes, n - No ")
#         if (input_upload == "y"):
#             uploadToOneDrive("../Source/output_file.txt")
#             print("Successfully uploaded file!")

#     elif (input_translate == "txt"): #Suppose if user has a file to be translated to
#         file_to_trans = input("Type in the name of the file that you want to be translated: ")
#         language_to_trans = input("Enter in the language that you want the text to be translated to: ")
#         translateFile(file_to_trans, "TranslatedFile.txt", language_to_trans) #why underlined, we defined translateFile in TextTest.py
    
    
    # else:  #Should we also give the option to the user for them to parse in pdf file? (useful if they have a certain document)
    #     #Note the pdf needs to be within the same folder
    #     pdf_ = input("Type in the name of pdf. Remeber to enter .pdf at end of file name: ") #Need to ensure valid pdf is entered
    #     pdfFileObj = open(pdf_, 'rb')
    #     pdfReader = PyPDF2.PdfFILErEADER(pdfFileObj)
    #     for i in range(pdfReader.numPages):
    #         pageObj = pdfReader.egtPage(i)
    #         print(pageObj.extractText())
    #     pdfFileObj.close()
 
    #Or instead should we convert pdf to text file and use existing features?
    #Also should we provide the ability for text to be converted into a pdf file that the user can utilize?