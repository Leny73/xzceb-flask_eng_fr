from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translates english text to french
    """
    return MyMemoryTranslator(source='en', target='fr').translate(english_text)

def french_to_english(french_text):
    """
    This function translates french text to english
    """
    return MyMemoryTranslator(source='fr', target='en').translate(french_text)
