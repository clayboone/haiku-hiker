list(map(lambda counts: print(f"{','.join(str(c) for c in counts)},{'Yes' if counts == [5, 7, 5] else 'No'}"), [[sum(word[i] in set('aeiouy') and word[i-1:i] not in set('aeiouy') for i in range(len(word))) for word in input().strip().split('/')]]))
