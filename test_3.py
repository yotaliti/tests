
from unittest import TestCase


def vote(votes):
    win = {}
    for v in votes:
        win[votes.count(v)] = v
    result = win[max(list(win.keys()))]
    return result


class TestMain(TestCase):
    def test_vote(self):
        for i, (votes, expected) in enumerate([
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
            ([4, 2, 3, 9, 2, 2, 9, 9], 9)
        ]):
            with self.subTest(i):
                result = vote(votes)
                self.assertEqual(expected, result)


