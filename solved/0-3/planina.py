n = int(input())

blah = 2
for _ in range(n):
    blah += (blah - 1)
print(blah**2)