import unittest
from socket import *
import json
import time
from pprint import pp
import sys


def client_message(server, port):
    soc = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    soc.connect((server, port))  # Соединиться с сервером

    timestamp = int(time.time())
    data = {  # Данные для отправки на сервак
        'action': 'presence',
        'time': timestamp,
        'type': 'status',
        'user': {
            'account_name': 'Drakaris',
            'status': 'Online'
        }
    }

    json_data = json.dumps(data)  # Перекидываем в json
    soc.send(json_data.encode('utf-8'))  # Кодируем

    data = soc.recv(1000)  # Получаем ответ сервака, цифра - буфер
    response = json.loads(data.decode("utf-8"))  # декодируем ответ сервака
    soc.close()  # прервать соединение
    return response

class TestClient(unittest.TestCase):

    def setUp(self):
        self.port = 7777
        self.server = '127.0.0.1'

    def test_server_response(self):
        normal_response = {'server_response': 200,
 'server_message': 'OK',
 'user': 'Drakaris',
 'status': 'Online'}
        self.assertEqual(client_message(self.server, self.port), normal_response)