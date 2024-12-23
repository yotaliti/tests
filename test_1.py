
from unittest import TestCase


def perimetr_of_squad(a: int) -> int:
    perimeter = a * 4  # Расчёт периметра

    return perimeter


class TestMain(TestCase):
    def test_perimetr_of_squad(self):
        for i, (a, expected) in enumerate([
            (6, 24),
            (7, 28),
            (11, 44)
        ]):
            with self.subTest(i):
                result = perimetr_of_squad(a)
                self.assertEqual(expected, result)
