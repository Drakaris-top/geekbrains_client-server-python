"""1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных."""

def print_task(words_data):
    for word in words_data:
        print(f'Тип:{type(word)} Значение:{word}')

words = ['разработка', 'cокет', 'декоратор']
print_task(words)

words_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                'c\u043e\u043a\u0435\u0442',
                '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
print_task(words_unicode)

