# from googletrans import Translator

# translator = Translator()

# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
# print(result)

from csv import reader
from googletrans import Translator
translator = Translator(service_urls=['translate.google.com','translate.google.co.kr',])

translator.translate('안녕하세요.')

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


# Print a basic CSV File
with open('Example.csv', 'r') as read_obj:
   # pass the file object to reader() to get the reader object
   csv_reader = reader(read_obj)
   # Iterate over each row in the csv using reader object
   for row in csv_reader:
       # row variable is a list that represents a row in csv
       print(row)