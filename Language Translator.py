#  Speech to text Recognizer

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#  LANGUAGE TRANSLATOR

from ibm_watson import LanguageTranslatorV3

url_lt = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/122d6074-4dfa-43a9-a116-25d96621c590'
apikey_lt = 'SFeNtsMPmYswHwnExP7MHS42YaILlR_H5rrOrVuUWhmh'

version_lt = '2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

from pandas.io.json import json_normalize

print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))

translation_response = language_translator.translate(text="Hello", model_id='en-es')  # The result is dictionary
#print(translation_response)

translation = translation_response.get_result()
print(translation)

spanish_translation = translation['translations'][0]['translation']
print(spanish_translation)
translation_new = language_translator.translate(text=spanish_translation, model_id='es-en').get_result()

translation_eng = translation_new['translations'][0]['translation']
print(translation_eng)

French_translation = language_translator.translate(
    text=translation_eng, model_id='en-fr').get_result()
print(French_translation['translations'][0]['translation'])


