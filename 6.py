"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое."""
import chardet

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as f:
    for word in words:
        f.write(f'{word}\n')

test_file = open('test_file.txt', 'rb').read()
print(f"Кодировка файла: {chardet.detect(test_file)['encoding']}\n")

test_file_utf8 = test_file.decode(chardet.detect(test_file)['encoding']).encode('utf-8').decode('utf-8')

print("Содиржимое файла:")
file_data = test_file_utf8.split('\n')
for line in file_data:
    print(line)