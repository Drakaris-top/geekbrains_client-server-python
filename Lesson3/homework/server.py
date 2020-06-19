# -*- coding: utf-8 -*-
"""
Функции сервера: принимает
сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту; имеет параметры командной
строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777); -a <addr> — IP-адрес
для прослушивания (по умолчанию слушает все доступные адреса).
"""
# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import json
from pprint import pp
import sys


def get_params(argv): #В этом скрипте работа с командной строкой сделана круче
    help = """Please set arguments -a adress -p port\n Example -a: 127.0.0.1 -p 8000)""" #подсказка

    if len(argv)>0 and argv[0] == '-h': #Получить подсказку
        print(help)
        return None

    else: #Получаем адрес сервера
        try:
            if argv[0] == '-a':
                addr = argv[1]
            else:
                addr = ''
        except:
            addr = ''

        try: # Получаем порт
            if argv[2] == '-p':
                port = int(argv[3])
            else:
                port = 7777
        except:
            port = 7777

    return addr, port

def start_server(addr, port):
    s = socket(AF_INET, SOCK_STREAM) #создаем сокет
    s.bind((addr, port)) # подключаемся
    s.listen(5)

    while True:
        client, addr = s.accept()
        data = client.recv(1000000)
        json_data = json.loads(data.decode('utf-8'))

        try: #Обрабатываем ошибки клиента
            if json_data['action'] != "presence":
                server_message = 'Action not allowed'
                response = 400

            elif json_data['time'] is None:
                server_message = 'Time error'
                response = 400

            elif json_data['type'] != 'status':
                server_message = 'status not allowed'
                response = 400

            elif json_data['user']['account_name'] is None:
                server_message = 'user_name not set'
                response = 404

            elif json_data['user']['status'] is None:
                server_message = 'status not allowed'
                response = 400

            else:
                server_message = 'OK'
                response = 200
        except: # Если у клиента ошибок нет, но что-то не так, то выводим ошибку сервера
            server_message = 'server_error'
            response = 500

        if response == 200: #Если все ок, отвечаем клиенту
            server_response = {'server_response': response,
                               'server_message': server_message,
                               'user': json_data['user']['account_name'],
                               'status': json_data['user']['status']}
        else:
            server_response = {'server_response': response,
                               'server_message': server_message}

        pp(server_response)
        client.send(json.dumps(server_response).encode('utf-8'))
        client.close()

if __name__ == '__main__':
    argv = sys.argv[1:]
    addr, port = get_params(argv)
    start_server(addr, port)
