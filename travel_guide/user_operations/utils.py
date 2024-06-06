# utils.py or views.py
from google.cloud import translate_v2 as translate
from django.conf import settings
from googletrans import Translator
from deep_translator import GoogleTranslator

# def translate_text(text, target_language='en'):
#     # try:
#     #     client = translate.Client(settings.GOOGLE_TRANSLATE_API_KEY)
#     #     result = client.translate(text, target_language=target_language)
#     #     translated_text = result['translatedText']
#     #     print(f"Translation successful: {translated_text}")
#     #     return translated_text
#     # except Exception as e:
#     #     print(f"Translation error: {e}")
#     #     return None
    
 
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     return translation.text

# def translate_text(text, target_language):
#     if target_language:
#         translator = GoogleTranslator(source='auto', target=target_language)
#     else:
#         translator = GoogleTranslator(source='auto', target='en')  # Default to English if target language is not provided

#     return translator.translate(text)

def translate_text(text, target_language='en'):
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)