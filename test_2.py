
from unittest import TestCase


def check_auth(login: str, password: str) -> str:
    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
        # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
    else:
        result = 'Доступ ограничен'
        # В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше

    return result


class TestMain(TestCase):
    def test_check_auth(self):
        for i, (l, p, expected) in enumerate([
            ('admin', 'password', 'Добро пожаловать'),
            ('admin', 'password', 'Добро пожаловать'),
            ('password', 'admin', 'Доступ ограничен')
        ]):
            with self.subTest(i):
                result = check_auth(l, p)
                self.assertEqual(expected, result)
