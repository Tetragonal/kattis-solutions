input()
print(len(list(filter(lambda x: x < 0, [int(x) for x in input().split()]))))
