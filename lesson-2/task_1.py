'''
    1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий
       выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
       формирующий новый «отчетный» файл в формате CSV. Для этого:
            a. Создать функцию get_data(), в которой в цикле осуществляется перебор
               файлов с данными, их открытие и считывание данных. В этой функции из
               считанных данных необходимо с помощью регулярных выражений извлечь
               значения параметров «Изготовитель системы»,  «Название ОС»,
               «Код продукта», «Тип системы». Значения каждого параметра поместить
               в соответствующий список. Должно получиться четыре списка — например,
               os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
               функции создать главный список для хранения данных отчета — например,
               main_data — и поместить в него названия столбцов отчета в виде списка:
               «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
               Значения для этих столбцов также оформить в виде списка и поместить в
               файл main_data (также для каждого файла);
            b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
               В этой функции реализовать получение данных через вызов функции get_data(),
               а также сохранение подготовленных данных в соответствующий CSV-файл;
            c. Проверить работу программы через вызов функции write_to_csv().
'''
from os import path
import re
import csv


LST_FILE = ('info_1.txt', 'info_2.txt', 'info_3.txt')

KEY_LIST = ('Изготовитель системы', 'Название ОС',
            'Код продукта', 'Тип системы')


def get_list_from_dict(dict={}):
    """Преобразует любой словарь в список списков
    Args:
        dict (dict, optional): Словарь. Defaults to {}.

    Returns:
        [list]: [список]
    """
    result = []

    cols = list(dict.keys())
    result.append(cols)
    inx = 0
    while True:  # Проходим по строкам
        data = []
        for col in cols:
            data.append(dict[col][inx] if len(dict[col]) > inx else '')
        if len(''.join(data)) == 0:
            break
        result.append(data)
        inx += 1
    return result


def get_data():

    result = {}
    for fn in LST_FILE:
        fn = path.join('lesson-2', fn)
        with open(fn, 'r', encoding='cp1251') as f:
            data = f.read()
            for key in KEY_LIST:
                if key not in result:
                    result[key] = []
                pattern = re.compile(rf'{key}:.+')
                # Почему-то не работает r'(?<=Изготовитель системы:\s+)\w+', хотя при тестировани регулярок это регурярка работает
                # Если не скложно подскажите почему?
                # Пришлось делать в "лоб".
                find_result = re.findall(pattern, data)[
                    0].replace(f'{key}:', '').strip()
                result[key].append(find_result)

    return get_list_from_dict(result)


def write_to_csv(file_name='file_name.csv'):

    data = get_data()
    print(data)
    with open(file_name, 'w', encoding='utf8') as f:
        f_writer = csv.writer(f, delimiter=';')
        f_writer.writerows(data)


write_to_csv('result.csv')
