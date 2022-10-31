

from googletrans import Translator   
class TxtToTxt:
    def translate(toTranslate, fileTo, chosenLanguage):                                   
        translator = Translator()
        # FIX LANGUAGE TAGS
        givenLanguage = translator.detect(toTranslate)          # detects original language in object format, use .lang for langtag
        languageTo = Translator.LANGUAGES[chosenLanguage]       # Converts Desired Languaage to LangTag
        
        translated1 = translator.translate(toTranslate, src = givenLanguage.lang, dest = languageTo)  # Creates translation object translating from src to dest
        print(translated1.text)
        file = open(fileTo, "w", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
        file.write(translated1.text)                                        # Write text from translated object
        file.close()                                                        # Closes file
        # #let's read the contents of the file now
        file = open(fileTo,"r", encoding = "utf-16")         # Opens translated file for reading
        print(file.read())                                                  # Prints the text in the written file
        file.close()    
=======
#     print(u"Text: {}".format(result["input"]))
#     print(u"Translation: {}".format(result["translatedText"]))
#     print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


# Print a basic CSV File
with open('Example.csv', 'r') as read_obj:
   # pass the file object to reader() to get the reader object
   csv_reader = reader(read_obj)
   # Iterate over each row in the csv using reader object
   for row in csv_reader:
       # row variable is a list that represents a row in csv
       print(row)

