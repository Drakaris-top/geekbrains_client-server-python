"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице."""

import subprocess
import chardet

def pingovalka(domain):
    args = ['ping', domain]

    pingovalka = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in pingovalka.stdout:
        char_detect = chardet.detect(line)
        encoded_line = line.decode(char_detect['encoding']).encode('utf-8')
        print(encoded_line.decode('utf-8'))

# pingovalka('yandex.ru')
pingovalka('youtube.com')