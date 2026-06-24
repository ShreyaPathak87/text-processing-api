from deep_translator import GoogleTranslator

def translate_text(text, language):
    return GoogleTranslator(
        source="auto",
        target=language
    ).translate(text)