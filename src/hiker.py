from functools import reduce


def main(input_string: str = ''):
    list(map(lambda counts: print(f"{','.join(str(c) for c in counts)},{'Yes' if counts == [5, 7, 5] else 'No'}"), [[reduce(lambda x, y: x + y, (word[i] in set('aeiouy') and word[i-1:i] not in set('aeiouy') for i in range(len(word))), 0) for word in input_string.strip().split('/')]]))

if __name__ == '__main__':  # pragma: no cover
    main(input('Enter your haiku: '))
