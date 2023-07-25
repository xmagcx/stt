from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
    ])
tranlated = translator.translate('hello.', dest='zh-CN')
print(tranlated)