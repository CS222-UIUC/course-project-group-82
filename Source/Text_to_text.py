# from googletrans import Translator

# translator = Translator()

# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
# print(result)

# from googletrans import Translator

# translator = Translator()

# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
# print(result)

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
