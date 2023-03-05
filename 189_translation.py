from translate import Translator

try:
    translator = Translator(to_lang='es')
    with open('/Users/deepaliyadav/Documents/_chat.txt', mode='r') as chat:
        text = chat.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('Couldn\'nt find the file')
    raise e
