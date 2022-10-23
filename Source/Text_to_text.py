# from googletrans import Translator

# translator = Translator()

# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
# print(result)
from googletrans import Translator
translator = Translator()
text1  = "はじめまして"
translated1 = translator.translate(text1, src = 'ja', dest = 'en')

print(translated1)

file = open("Pretranslation.txt", "w")
file.write(text1)
file.close()

file = open("Prosttranslation.txt", "w")
file.write(translated1)
file.close()


#let's read the contents of the file now
file = open("geeksforgeeks.txt","r")
print(file.read())

# def translate_text(target, text):
#     # """Translates text into the target language.

#     # Target must be an ISO 639-1 language code.
#     # See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     # """
#     import six
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     if isinstance(text, six.binary_type):
#         text = text.decode("utf-8")

#     # Text can also be a sequence of strings, in which case this method
#     # will return a sequence of results for each text.
#     result = translate_client.translate(text, target_language=target)

#     print(u"Text: {}".format(result["input"]))
#     print(u"Translation: {}".format(result["translatedText"]))
#     print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
