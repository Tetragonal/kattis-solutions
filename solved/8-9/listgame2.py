from math import *
import itertools

n = int(raw_input())
x = n
factors = {}
count = 0
done = False
curr = 2
while curr <= 1+int(floor(sqrt(n))):
    if n % curr == 0:
        count += 1
        n //= curr
        if curr not in factors: factors[curr] = 0
        factors[curr] += 1
    else: curr += 1

if n != 1:
    if n not in factors: factors[n] = 0
    factors[n] += 1

keys = []
values = []
for k,v in factors.items():
    keys.append(k)
    values.append(v-1)

primes = set(keys)

factors = set()

for tup in itertools.product(*[range(x+1) for x in values]):
    total = 1
    if sum(tup) == 1: continue
    for idx, count in enumerate(tup):
        total *= keys[idx]**count
    factors.add(total)

factors = list(factors)
factors.sort()

arr = [0] * len(factors)

f_to_i = {f: i for i, f in enumerate(factors)}

for i in range(len(factors)):
    factor = factors[i]
    for j in range(len(factors), 0, -1):
        j -= 1
        factor_j = factors[j]
        if factor_j % factor != 0: continue
        div = factor_j // factor
        if div not in f_to_i: continue
        idx = f_to_i[div]
        arr[j] = max(arr[j], 1 + arr[idx])

print(max(arr)-1 + len(keys))