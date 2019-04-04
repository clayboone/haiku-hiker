class Haiku(object):

    vowels = list('aeiouy')
    correct_pattern = [5, 7, 5]

    def __init__(self, haiku=None):
        self.input_string = haiku

    @staticmethod
    def count_syllables(word):
        """Return number of syllables in a string as an integer"""
        characters_in_word = list(word)
        prev = None
        count = 0

        for char in characters_in_word:
            if char in Haiku.vowels and prev not in Haiku.vowels:
                count += 1

            prev = char

        return count

    @property
    def syllables(self):
        """Return a list of the number of syllable in each part of a
        haiku as an array.
        """
        counts = []

        for part in self.input_string.split('/'):
            counts.append(Haiku.count_syllables(part))

        return counts

    @property
    def isCorrect(self):
        """Return whether or not a list of syllable counts can be
        considrered a correct haiku.
        """

        if len(self.syllables) != len(Haiku.correct_pattern):
            return False

        for i, _ in enumerate(self.syllables):
            if self.syllables[i] != Haiku.correct_pattern[i]:
                return False

        return True

    def __repr__(self):
        """Build the output string according to the example output in
        the spec. The `readme.txt` indicates that a simple 'Y' or 'N'
        should be used, but the example output shows the full 'Yes'
        and 'No' words. I'll use the words, as that's the exact type
        of string requested, and it can be grepped down to 'Y' or 'N'
        anyways.
        """

        if self.input_string is None:
            raise ValueError('No input string for this Haiku was supplied')

        ret = self.syllables[:]
        ret.append('Yes' if self.isCorrect else 'No')

        return ','.join(str(x) for x in ret)


if __name__ == '__main__':  # pragma: no cover
    haiku = Haiku(input('Enter your haiku: '))

    print(f'Output: {haiku}')
