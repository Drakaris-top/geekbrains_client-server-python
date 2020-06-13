"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

words = ['attribute', 'класс', 'функция']

for word in words:
    try:
        byte_word = word.encode('ascii')
        print(f"{byte_word} - OK!")
    except:
        print(f"{word}  - невозможно записать в байтовом формате")