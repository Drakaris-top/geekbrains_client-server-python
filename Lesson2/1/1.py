"""Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.
*



* Проверить работу программы через вызов функции write_to_csv()."""

import glob
import chardet
import re
import csv

files_path = glob.glob('1/res/*.txt')

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

def find_value_in_file(search_string, file):
    """В этой функции из считанных данных необходимо
с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы»."""
    string_with_value = re.findall(f'{search_string}.*$', file, re.MULTILINE)
    value = re.split(r':', string_with_value[0])[1].strip()
    return value



def get_data():
    """Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
    их открытие и считывание данных."""
    main_data_values = []
    """В этой же функции создать главный список для хранения
    данных отчета — например, main_data — и поместить в него названия столбцов отчета
    в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы»."""
    main_data_headers = ['Изготовитель системы','Название ОС','Код продукта','Тип системы']
    for file in files_path:
        opened_file = open(file, 'rb').read()
        file_encoding = chardet.detect(opened_file)['encoding']
        opened_file_utf_8 = opened_file.decode(file_encoding).encode('utf-8').decode('utf-8')



        os_prod = find_value_in_file(main_data_headers[0], opened_file_utf_8)
        os_name = find_value_in_file(main_data_headers[1], opened_file_utf_8)
        os_code = find_value_in_file(main_data_headers[2], opened_file_utf_8)
        os_type = find_value_in_file(main_data_headers[3], opened_file_utf_8)

        """Значения каждого параметра поместить в соответствующий список.
        Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
        os_type_list."""
        os_prod_list.append(os_prod)
        os_name_list.append(os_name)
        os_code_list.append(os_code)
        os_type_list.append(os_type)

        """Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);"""
        file_main_data_values = [os_prod, os_name, os_code, os_type]
        main_data_values.append(file_main_data_values)
        main_file_name = file.split('/')[2].split('.')[0]
        main_file = open(f'1/main_data_files/main_file_{main_file_name}.txt', 'w', encoding='utf-8')
        for counter, header in enumerate(main_data_headers):
            main_file.write(f'{header}: {file_main_data_values[counter]}\n')

    return main_data_headers, main_data_values

csv_report = open('1/main_data_report.csv', 'w', encoding='utf-8')
csv_report.close()

def write_to_csv(report_link):
    """* Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;"""
    data_headers, data_values = get_data()
    with open(report_link, 'w') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(data_headers)
        f_writer.writerows(data_values)

write_to_csv('1/main_data_report.csv')