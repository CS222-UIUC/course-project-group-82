from csv import reader
from googletrans import Translator  
from Source.Text_To_Text import TxtToTxt

#Test 1 (Check if one letter word text is fine)
def test_single_words():                              
    translator = Translator()
    translated_text_one = translator.translate("Hello", src = translator.detect("Hello").lang, dest = "es")
    assert(translated_text_one.text == "Hola")
    translated_text_two = translator.translate("Hola", src = translator.detect("Hola").lang, dest = "en")
    # assert(translated_text_two.text == "Bonjour")
    # detects 'Bonjour' as English
    print(translator.detect("Hola")) #Ask about this in meeting
    print("passed") #Ask about this in meeting
    #assert(translated_text_two.text == "Hello")

def test_multiple_words():                              
    translator = Translator()
    translated_text_one = translator.translate("I am feeling very tired today", src = translator.detect("I am feeling very tired today").lang, dest = "it")
    print(translated_text_one.text)
    assert(translated_text_one.text == "Oggi mi sento molto stanco")
    translated_text_two = translator.translate("Ich laufe jetzt", src = translator.detect("Ich laufe jetzt").lang, dest = "en")
    assert(translated_text_two.text == "I'm running now")

def test_several_sentences(): #Also tests punctuation marks                              
    translator = Translator()
    to_translate = "I am feeling very tired today. How are you doing? What are you up to? What a Surprise!"
    translated_text_one = translator.translate(to_translate, src =  translator.detect(to_translate).lang, dest ="es"); 
    assert(translated_text_one.text == "Me siento muy cansado hoy.¿Como estas?¿Qué estás haciendo?¡Qué sorpresa!")

    to_translate_two = "Wow je ne savais pas ça ! Qui vous en a parlé ? Que devons-nous faire maintenant?"
    translated_text_two = translator.translate(to_translate_two, src = translator.detect(to_translate_two).lang, dest = "en")
    assert(translated_text_two.text == "Wow I didn't know that!Who told you about it?What should we do now?")

    to_translate_three = "Ich bin jetzt sehr hungrig. Wo möchtest du essen? Wie weit ist es von hier?"
    translated_text_three = translator.translate(to_translate_three, src =  translator.detect(to_translate_three).lang, dest = "zh-cn")
    # I checked, the text looks the exact same to me. Unsure of the case, assume it is because we compare string exactly.
    assert(translated_text_three.text == "我现在很饿。你想去哪里吃饭？离这有多远？")
    
def translateText(): # Checks text to file
    txtTranslator = TxtToTxt()
    file = open("fileTo.txt", "w", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
    file.write("")                                        # Write text from translated object
    file.close() 
    file = open("fileSecond.txt", "w", encoding = "utf-16")        # Opens file with name, , uses write command, encodes to utf-16 
    file.write("")                                        # Write text from translated object
    file.close() 

    to_translate = "I am feeling very tired today. How are you doing? What are you up to? What a Surprise!"
    txtTranslator.translateText(to_translate, "fileTo.txt", "Spanish") #Text-To-File Test
    txtTranslator.translateFile("test.txt", "fileSecond.txt", "Spanish") #File-To-File Test
    to_translate = "bonjour"
    txtTranslator.translateText(to_translate, "fileTo2.txt", "English") #Text-To-File Test
    to_translate = "freiheit"
    txtTranslator.translateText(to_translate, "fileTo3.txt", "English") #Text-To-File Test
    to_translate = "bueno"
    txtTranslator.translateText(to_translate, "fileTo4.txt", "English") #Text-To-File Test
    txtTranslator.translateFile("test.txt", "fileSecond.txt", "Spanish") #File-To-File Test
    txtTranslator.translateFile("DeBelloGallico.txt", "TheGallicWar.text", "English")

#test_single_words()
#test_multiple_words()
#test_several_sentences()
#translateText()
