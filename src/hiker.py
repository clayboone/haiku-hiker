from functools import reduce


def main(input_string: str = ''):
    vowels, words, reducer = set('aeiouy'), input_string.strip().split('/'), lambda x, y: x + y
    counts = tuple(reduce(reducer, (word[i] in vowels and word[i-1:i] not in vowels for i in range(len(word))), 0) for word in words)
    print(f"{','.join(str(c) for c in counts)},{'Yes' if counts == (5, 7, 5) else 'No'}")


if __name__ == '__main__':  # pragma: no cover
    main(input('Enter your haiku: '))
