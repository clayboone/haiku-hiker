from functools import reduce


class Haiku:

    VOWELS = list('aeiouy')
    CORRECT_PATTERN = (5, 7, 5)

    def __init__(self, s: str = ''):
        self._input_string = s.strip()

    @staticmethod
    def count_syllables(word: str) -> int:
        """Return the number of syllables in a string."""
        return reduce(lambda total, cur: total + cur, (word[i] in Haiku.VOWELS and word[i-1:i] not in Haiku.VOWELS for i in range(len(word))), 0)

    @property
    def syllables(self) -> tuple:
        """Return a tuple of the number of syllables."""
        return tuple(self.count_syllables(p) for p in self._input_string.split('/'))

    def is_correct(self) -> bool:
        """Return True if input is a correct haiku, otherwise False."""
        return self.syllables == self.CORRECT_PATTERN

    def calculate(self) -> str:
        """Return a string of the comma-separated number of syllables followed
        'Yes' for a correct haiku or 'No' for an incorrect haiku.
        """
        return f"{','.join(str(s) for s in self.syllables)},{'Yes' if self.is_correct() else 'No'}"


if __name__ == '__main__':  # pragma: no cover
    haiku = Haiku(input('Enter your haiku: '))
    print(haiku.calculate())
