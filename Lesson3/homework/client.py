# -*- coding: utf-8 -*-
"""
Функции клиента: сформировать presence-сообщение; отправить сообщение серверу; получить ответ сервера;
разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.
"""
# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *
import json
import time
from pprint import pp
import sys

def get_params():
        argv = sys.argv[1:] # Получаем параметры

        hint = """Please set arguments -s server -p port\n Example -s: 127.0.0.1 -p 8000)""" #Подсказка

        if len(argv) == 0: #Если нет параметров
                print(hint)
        try: #Получаем параметры сервера
                if argv[0] == '-s':
                        server = argv[1]
                else:
                        print('Server not set')
                        print(hint)
                        return None
        except:
                print('Server not set')
                print(hint)
                return None

        try: #Получаем параметры порта
                if argv[2] == '-p':
                        port = int(argv[3])
                else:
                        port = 7777
        except:
                port = 7777
        return server, port

def client_message(server, port):
        soc = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
        soc.connect((server, port))   # Соединиться с сервером

        timestamp = int(time.time())
        data = { # Данные для отправки на сервак
                'action': 'presence',
                'time': timestamp,
                'type': 'status',
                'user': {
                        'account_name':  'Drakaris',
                        'status': 'Online'
                }
        }

        json_data = json.dumps(data) #Перекидываем в json
        soc.send(json_data.encode('utf-8')) #Кодируем

        data = soc.recv(1000000) #Получаем ответ сервака, цифра - буфер
        pp(json.loads(data.decode("utf-8"))) #декодируем ответ сервака
        soc.close() # pfrhsdftv соединение

if __name__ == '__main__':
    server, port = get_params() #получаем парамтеры сервера и порта
    client_message(server, port) #отправляем сообщение на сервак