import unittest

from hiker import Haiku


class TestHaiku(unittest.TestCase):

    test_haikus = [
        {
            'input_string': 'happy purple frog/eating bugs in the marshes/get indigestion',
            'syllables': (5, 7, 5),
            'is_correct': True,
            'calculate': '5,7,5,Yes'
        },
        {
            'input_string': 'computer programs/the bugs try to eat my code/i will not let them',
            'syllables': (5, 8, 5),
            'is_correct': False,
            'calculate': '5,8,5,No'
        }
    ]

    def test_count_syllables(self):
        # Empty inputs.
        self.assertEqual(Haiku.count_syllables(''), 0)

        # Troublesome one- and two-letter inputs.
        self.assertEqual(Haiku.count_syllables('a'), 1)
        self.assertEqual(Haiku.count_syllables('a a '), 2)
        self.assertEqual(Haiku.count_syllables(' a a'), 2)
        self.assertEqual(Haiku.count_syllables('b'), 0)
        self.assertEqual(Haiku.count_syllables('b b '), 0)
        self.assertEqual(Haiku.count_syllables(' b a'), 1)

        # Normal words.
        self.assertEqual(Haiku.count_syllables('happy'), 2)
        self.assertEqual(Haiku.count_syllables('abaaaabaaaba'), 4)
        self.assertEqual(Haiku.count_syllables('happy purple frog'), 5)

        # Extra whitespace.
        self.assertEqual(Haiku.count_syllables('         happy'), 2)
        self.assertEqual(Haiku.count_syllables('happy         '), 2)
        self.assertEqual(Haiku.count_syllables('\t\t happy\r\n'), 2)

    def test_empty_object_instantiation_returns_a_haiku_object(self):
        self.assertIsInstance(Haiku(), Haiku)

    def test_syllables_property(self):
        for haiku in self.test_haikus:
            obj = Haiku(haiku['input_string'])
            self.assertEqual(obj.syllables, haiku['syllables'])

    def test_is_correct(self):
        for haiku in self.test_haikus:
            obj = Haiku(haiku['input_string'])
            self.assertEqual(obj.is_correct(), haiku['is_correct'])

    def test_calculate(self):
        for haiku in self.test_haikus:
            obj = Haiku(haiku['input_string'])
            self.assertEqual(obj.calculate(), haiku['calculate'])


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
