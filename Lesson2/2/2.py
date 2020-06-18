"""Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
* Создать функцию write_order_to_json(), в которую передается 5 параметров
— товар (item), количество (quantity), цена (price), покупатель (buyer),дата (date).
Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
* Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра."""

from faker import Faker
import json

faker = Faker()

def generate_order():
    item = f'Book:{faker.isbn10()}'
    quantity = faker.random_int(0, 3)
    price = faker.random_int(5, 100) * quantity
    buyer = f'{faker.first_name()} {faker.last_name()}'
    date = f'{faker.date_between(start_date="-1y", end_date="today")}'
    return item, quantity, price, buyer, date


def write_order_to_json(item, quantity, price, buyer, date):
    data_dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    add_order = {'orders': data_dict}
    with open('orders.json', 'w') as f:
        json.dump(add_order, f, indent=4)


item, quantity, price, buyer, date = generate_order()
write_order_to_json(item, quantity, price, buyer, date)