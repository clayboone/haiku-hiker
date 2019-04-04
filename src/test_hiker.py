from hiker import Haiku
import unittest


class TestHaiku(unittest.TestCase):

    test_haikus = [
        {
            'input_string': 'happy purple frog/eating bugs in the marshes/get '
            'indigestion',
            'syllables': [5, 7, 5],
            'isCorrect': True,
            'repr': '5,7,5,Yes'
        },
        {
            'input_string': 'computer programs/the bugs try to eat my code/i '
            'will not let them',
            'syllables': [5, 8, 5],
            'isCorrect': False,
            'repr': '5,8,5,No'
        }
    ]

    def test_count_syllables(self):
        self.assertEqual(Haiku.count_syllables('happy'), 2)
        self.assertEqual(Haiku.count_syllables(''), 0)
        self.assertEqual(Haiku.count_syllables('abaaaabaaaba'), 4)
        self.assertEqual(Haiku.count_syllables('happy purple frog'), 5)

    def test_raises_valueerror_on_empty_input(self):
        with self.assertRaises(ValueError):
            print(Haiku())

    def test_syllables_property(self):
        obj = Haiku()

        for haiku in self.test_haikus:
            obj.input_string = haiku['input_string']
            self.assertEqual(obj.syllables, haiku['syllables'])

    def test_isCorrect(self):
        obj = Haiku()

        for haiku in self.test_haikus:
            obj.input_string = haiku['input_string']
            self.assertEqual(obj.isCorrect, haiku['isCorrect'])

    def test_repr(self):
        obj = Haiku()

        for haiku in self.test_haikus:
            obj.input_string = haiku['input_string']
            self.assertEqual(str(obj), haiku['repr'])


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
