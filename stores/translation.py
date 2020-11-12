from modeltranslation.translator import translator, TranslationOptions

from .models import Store, StoreAddress


class StoreTranslationOptions(TranslationOptions):
    fields = ['name', 'description', 'manager_name']


class StoreAddressTranslationOptions(TranslationOptions):
    fields = ['line1', 'state']


translator.register(Store, StoreTranslationOptions)
translator.register(StoreAddress, StoreAddressTranslationOptions)
