from googletrans import Translator

translator = Translator()

result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
print(result)