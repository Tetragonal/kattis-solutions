have = list(map(int,input().split()))
want = [1, 1, 2, 2, 2, 8]
print(' '.join(map(lambda x: str(x[1]-x[0]), zip(have,want))))
