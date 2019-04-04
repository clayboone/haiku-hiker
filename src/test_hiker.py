from hiker import *
import unittest


class TestHiker(unittest.TestCase):

    haikus = [
        'happy purple frog/eating bugs in the marshes/get indigestion',
        'computer programs/the bugs try to eat my code/i will not let them'
    ]

    def test_count_syllables(self):
        self.assertEqual(count_syllables('happy'), 2)
        self.assertEqual(count_syllables(''), 0)
        self.assertEqual(count_syllables('abaaaabaaaba'), 4)
        self.assertEqual(count_syllables('happy purple frog'), 5)

    def test_syllable_counts_as_list(self):
        self.assertEqual(syllable_counts_as_list(self.haikus[0]), [5, 7, 5])
        self.assertEqual(syllable_counts_as_list(self.haikus[1]), [5, 8, 5])

    def test_ishaiku(self):
        self.assertEqual(ishaiku([5, 7]), False)
        self.assertEqual(ishaiku([5, 7, 5, 5]), False)
        self.assertEqual(ishaiku([1, 2, 3]), False)
        self.assertEqual(ishaiku([5, 7, 5]), True)

    def test_build_output(self):
        self.assertEqual(build_output(self.haikus[0]), '5,7,5,Yes')
        self.assertEqual(build_output(self.haikus[1]), '5,8,5,No')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
