"""
Фамилия     Имя         Часов   Ставка
Иванов      Иван        45      400
Докукин     Филимон     20      1000
Ромашкин    Сидор       45      500
"""

from collections import namedtuple
import unittest

Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))


def get_salary(line):
    line = line.split()
    if line:
        data = Salary(*line)
        full_name = ' '.join((data.surname, data.name))
        salary = int(data.worked) * int(data.rate)
        res = (full_name, salary)
    else:
        res = ()
    return res


class TestSalary(unittest.TestCase):

    def setUp(self):
        self.data = 'Лютиков Руслан 60 1000'

    def test_get_salary_sum(self):
        self.assertEqual(get_salary(self.data), ('Лютиков Руслан', 60000))

    def test_get_salary_full_name(self):
        self.assertEqual(get_salary(self.data)[0], 'Лютиков Руслан')

    def test_get_salary_empty(self):
        self.assertEqual(get_salary(''), ())

if __name__ == '__main__':
    unittest.main()