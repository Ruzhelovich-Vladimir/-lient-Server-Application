'''
2. Задание на закрепление знаний по модулю json. Есть файл orders 
    в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий 
    его заполнение данными. Для этого:
        a. Создать функцию write_order_to_json(), в которую передается 
           5 параметров — товар(item), количество(item), цена(price), 
           покупатель(buyer), дата(date). Функция должна предусматривать 
           запись данных в виде словаря в файл orders.json. При записи 
           данных указать величину отступа в 4 пробельных символа
        b. Проверить работу программы через вызов функции write_order_to_json() 
           с передачей в нее значений каждого параметра.
'''

from datetime import datetime
import json
import os


def write_order_to_json(item, qty, price, buyer, date=datetime.now()):

    _dict = {
        'item': item,
        'qty': qty,
        'price': price,
        'buyer': buyer,
        'date': str(date)
    }

    with open(os.path.join(os.path.abspath(os.curdir), 'orders.json'), 'r', encoding='utf-8') as f:
        dict_to_json = json.load(f)

    dict_to_json['orders'].append(_dict)

    with open(os.path.join(os.path.abspath(os.curdir), 'orders.json'), 'w', encoding='utf-8') as f:
        json.dump(dict_to_json, f, sort_keys=False, indent=4)


for inx in range(1, 10):
    write_order_to_json(f'Товар{inx}', inx, inx*10, 'Иванов')
