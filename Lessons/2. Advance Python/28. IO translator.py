from translate import Translator

translator = Translator(to_lang="vi")
try:
    with open("./test.txt", "r") as f:
        words = f.read()
        translation = translator.translate(words)
        with open("./test2.txt", "a", encoding="UTF8") as e:
            w = e.write(translation)
except FileNotFoundError:
    print("Check your file mofo")