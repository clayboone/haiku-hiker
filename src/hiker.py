def count_syllables(word):
    """Return number of syllables from word as an integer"""
    vowels = list('aeiouy')
    characters_in_word = list(word)
    prev = None
    count = 0

    for char in characters_in_word:
        if char in vowels and prev not in vowels:
            count += 1

        prev = char

    return count


def syllable_counts_as_list(haiku):
    """Return a list of the number of syllable in each part of a
    haiku as an array.
    """
    counts = []

    for part in haiku.split('/'):
        counts.append(count_syllables(part))

    return counts


def ishaiku(counts_list):
    """Return whether or not a list of syllable counts can be
    considrered a correct haiku.
    """
    correct_pattern = [5, 7, 5]

    if len(counts_list) != len(correct_pattern):
        return False

    for i, _ in enumerate(counts_list):
        if counts_list[i] != correct_pattern[i]:
            return False

    return True


def build_output(haiku):
    """Build the output string according to the example output in
    the spec. The `readme.txt` indicates that a simple 'Y' or 'N'
    should be used, but the example output shows the full 'Yes'
    and 'No' words. I'll use the words, as that's the exact type
    of string requested, and it can be grepped down to 'Y' or 'N'
    anyways.
    """

    a = syllable_counts_as_list(haiku)
    a.append('Yes' if ishaiku(a) else 'No')

    return ','.join(str(x) for x in a)


if __name__ == '__main__':
    """Demo on using the functions.

    These lines are not counted towards the code coverage.
    """

    haiku = 'happy purple frog/eating bugs in the marshes/get indigestion'

    print(f'Input: {haiku}')
    print()
    print(f'Output: {build_output(haiku)}')
