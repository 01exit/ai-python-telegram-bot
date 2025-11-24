from .multilang import translations

def translation(lang: str, key: str):
    return translations.get(lang, translations["en"]).get(key, key)