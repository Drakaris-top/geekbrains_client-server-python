from unittest import TestCase

def sum_kv_ij(i, j):
    """Сумма квадратов."""
    return i * i + j * j


def val_compare(val_1, val_2):
    """Сравнение значений."""
    return val_1 > val_2


class Plane:
    """class"""
    pass


class Car:
    """class"""
    pass


def is_compare(val_1, val_2):
    return val_1 is val_2


def is_none(val_1):
    val_2 = val_1
    return val_2


class TestSumKV(TestCase):

    def test_equal(self):
        self.assertEqual(sum_kv_ij(2, 3), 13)

    def test_not_equal(self):
        self.assertNotEqual(sum_kv_ij(2, 3), 10)

    def test_true(self):
        self.assertTrue(val_compare(10, 3), True)

    def test_false(self):
        self.assertFalse(val_compare(10, 30), False)

    def test_is(self):
        self.assertIs(is_compare(Plane(), Plane()), False)

    def test_is_not(self):
        self.assertIsNot(is_compare(Plane(), Plane()), True)

    def test_is_none(self):
        self.assertIsNone(is_none(None), True)

    def test_is_not_none(self):
        self.assertIsNotNone(is_none('string'), True)

    def test_in(self):
        self.assertIn(1, [1, 2, 3])

    def test_not_in(self):
        self.assertNotIn(4, [1, 2, 3])

    def test_is_instance(self):
        self.assertIsInstance(Plane(), Plane)

    def test_not_is_instance(self):
        self.assertNotIsInstance(Plane(), Car)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 // 0

