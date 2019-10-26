import functools, sys
list(map(lambda counts: print(f"{','.join(str(c) for c in counts)},{'Yes' if counts == [5, 7, 5] else 'No'}"), [[functools.reduce(lambda x, y: x + y, (word[i] in set('aeiouy') and word[i-1:i] not in set('aeiouy') for i in range(len(word))), 0) for word in sys.stdin.readlines(1)[0].strip().split('/')]]))
