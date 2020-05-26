#  Speech to text Recognizer

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0e878f97-9346-4c23-8921-6a8608b5b062"

iam_apikey_s2t = "CgKWu_0ff411WxmKBrQ3a79L9Axxuq8NKZz75eay1YXc"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

filename = 'E:/AI_ML/PolynomialRP1.mp3'

with open(filename, mode="rb") as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

print(response.result)

from pandas.io.json import json_normalize

print(json_normalize(response.result['results'], 'alternatives'))
#print(response)
recognized_text = response.result['results'][0]["alternatives"][0]["transcript"]
print(type(recognized_text))
