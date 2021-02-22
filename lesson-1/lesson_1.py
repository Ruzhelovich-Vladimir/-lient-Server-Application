'''
    1. Каждое из слов «разработка», «сокет», «декоратор» 
    представить в строковом формате и проверить тип и 
    содержание соответствующих переменных. Затем с
    помощью онлайн-конвертера преобразовать строковые 
    представление в формат Unicode и также проверить 
    тип и содержимое переменных.
'''


def task_1():
    print(f'{"#"*5}   Задание №1  {"#"*50}')
    str_1 = 'разработка'
    str_2 = 'сокет'
    str_3 = 'декоратор'

    for val in (str_1, str_2, str_3):
        print(f'"{val}" type is {type(val).__name__}')

    uni_1 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
    uni_2 = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
    uni_3 = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

    for val in (uni_1, uni_2, uni_3):
        print(f'"{val}" type is {type(val).__name__}, value is "{val.decode()}"')


task_1()
'''
Результат:
#####   Задание №1  ##################################################
"разработка" type is str
"сокет" type is str
"декоратор" type is str
"b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'" type is bytes, value is "разработка"
"b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'" type is bytes, value is "сокет"
"b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'" type is bytes, value is "декоратор"
'''

'''
    2. Каждое из слов «class», «function», «method» 
    записать в байтовом типе без преобразования в 
    последовательность кодов (не используя методы 
    encode и decode) и определить тип, содержимое и 
    длину соответствующих переменных.
'''


def task_2():
    print(f'{"#"*5}   Задание №2  {"#"*50}')

    byte_1 = b'class'
    byte_2 = b'function'
    byte_3 = b'method'

    for val in (byte_1, byte_2, byte_3):
        print(f'"{val}" type is {type(val).__name__}, len={len(val)}')


task_2()
'''
Результат:
#####   Задание №2  ##################################################
"b'class'" type is bytes, len=5
"b'function'" type is bytes, len=8
"b'method'" type is bytes, len=6
'''

'''
    3. Определить, какие из слов «attribute», «класс», 
    «функция», «type» невозможно записать в байтовом типе.
'''


def task_3():
    print(f'{"#"*5}   Задание №3  {"#"*50}')
    str_list = ['attribute', 'класс', 'функция', 'type']
    # Понятно, что кирилицу, но всёравно реализую алгритм
    for _str in str_list:
        try:
            _str.encode('ascii')
        except:
            print(f'Строку "{_str}" нельзя записать ввиде byte строки')


task_3()
'''
#####   Задание №3  ##################################################
Строку "класс" нельзя записать ввиде byte строки
Строку "функция" нельзя записать ввиде byte строки
'''

'''
    4. Преобразовать слова «разработка», «администрирование»,
    «protocol», «standard» из строкового представления в 
    байтовое и выполнить обратное преобразование (используя 
    методы encode и decode).
'''


def task_4():
    print(f'{"#"*5}   Задание №4  {"#"*50}')
    str_list = ['разработка', 'администрирование', 'protocol', 'standard']
    for _str in str_list:
        byte_str = _str.encode('utf8')
        uni_str = byte_str.decode('utf-8')
        print(f'byte string:{byte_str}; unicode sring:{uni_str}')


task_4()
'''
#####   Задание №4  ##################################################
byte string:b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'; unicode sring:разработка
byte string:b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'; unicode sring:администрирование
byte string:b'protocol'; unicode sring:protocol
byte string:b'standard'; unicode sring:standard
'''

'''
    5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
    преобразовать результаты из байтовового в строковый тип 
    на кириллице.
'''


def task_5():
    print(f'{"#"*5}   Задание №5  {"#"*50}')
    import subprocess

    args = ['ping', '-c3', 'yandex.ru']
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for _str in subproc_ping.stdout:
        print(_str.decode('utf-8'))


task_5()
'''
Результат:
#####   Задание №5  ##################################################
PING yandex.ru (77.88.55.77) 56(84) bytes of data.

64 bytes from yandex.ru (77.88.55.77): icmp_seq=1 ttl=55 time=39.9 ms

64 bytes from yandex.ru (77.88.55.77): icmp_seq=2 ttl=55 time=40.5 ms

64 bytes from yandex.ru (77.88.55.77): icmp_seq=3 ttl=55 time=40.0 ms



--- yandex.ru ping statistics ---

3 packets transmitted, 3 received, 0% packet loss, time 2004ms

rtt min/avg/max/mdev = 39.882/40.138/40.546/0.291 ms
'''

'''
    6. Создать текстовый файл test_file.txt, заполнить его
    тремя строками: «сетевое программирование», «сокет»,
    «декоратор». Проверить кодировку файла по умолчанию. 
    Принудительно открыть файл в формате Unicode и вывести 
    его содержимое.
'''


def task_6():
    print(f'{"#"*5}   Задание №6  {"#"*50}')

    str_list = ['сетевое программирование', 'сокет', 'декоратор']
    file_name = 'lesson_1_task_6.txt'

    with open(file_name, 'w') as f:
        for _str in str_list:
            f.write(f'{_str}\n')

    with open(file_name, 'r', encoding='utf-8') as f:
        print(f.read())


task_6()
'''
#####   Задание №6  ##################################################
сетевое программирование
сокет
декоратор

Кодировка по умолчанию utf-8
'''
