from csv import reader
from googletrans import Translator
from googletrans import Translator

#Test 1 (Check if one letter word text is fine)
def test_single_words():
    transalted_text_one = translator.translate("Hello", src = translator.detect("Hello").lang, dest = "es")
    assert(translated_text_one == "Hola")
    transalted_text_two = translator.translate("Bonjour", src = translator.detect("Bonjour").lang, dest = "en")
    assert(translated_text_two == "Hello")

def test_multiple_words():
    transalted_text_one = translator.translate("I am feeling very tired today", src = translator.detect("I am feeling very tired today").lang.lang, dest = "it")
    assert(translated_text_one == "Mi sento molto stanco oggi")
    transalted_text_two = translator.translate("Ich laufe jetzt", src = translator.detect("Ich laufe jetzt"), dest = "en")
    assert(transalted_text_two == "I am running now")

def test_several_sentences(): #Also tests punctuation marks
    to_translate = "I am feeling very tired today. How are you doing? What are you up to? What a Surprise!"
    transalted_text_one = translator.translate(to_translate, src =  translator.detect(to_translate), dest ="es"); 
    assert(transalted_text_one == "Me siento muy cansada hoy. ¿Como estas? ¿Qué estás haciendo? Qué sorpresa")

    to_translate_two = "Wow je ne savais pas ça ! Qui vous en a parlé ? Que devons-nous faire maintenant?"
    transalted_text_two = translator.translate(to_translate_two, src = translator.detect(to_translate_two), dest = "en")
    assert(transalted_text_two == "Wow I didn't know that! Who told you about it? What should we do now?")

    to_translate_three = "Ich bin jetzt sehr hungrig. Wo möchtest du essen? Wie weit ist es von hier?"
    transalted_text_three = translator.translate(to_translate_three, src =  translator.detect(to_translate_three), dest = "zh-cn")
    assert(transalted_text_three == "我现在很饿。 你想去哪里吃饭？ 离这有多远？")
