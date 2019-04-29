import sys
from math import ceil

for line in sys.stdin:
    s = set()
    num = int(line)
    total = 0
    for i in range(1, ceil(num**0.5)+1):
        if num == i: break
        if num % i == 0:
            s.add(i)
            if i != 1:
                s.add(num//i)
    total = sum([x for x in s])
    if total == num:
        print(num, 'perfect')
    elif abs(total - num) <= 2:
        print(num, 'almost perfect')
    else:
        print(num, 'not perfect')