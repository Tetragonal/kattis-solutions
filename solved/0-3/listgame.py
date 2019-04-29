from math import *

n = int(input())
count = 0
done = False
while not done:
    done = True
    for i in range(2, 1+floor(sqrt(n))):
        if n % i == 0:
            count += 1
            n //= i
            done = False
            break
print(1+count)
