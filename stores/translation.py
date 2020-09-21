from modeltranslation.translator import translator, TranslationOptions

from .models import Store


class StoreTranslationOptions(TranslationOptions):
    fields = ['name', 'description','manager_name']



translator.register(Store, StoreTranslationOptions)
