Q, M, S, L = [int(x) for x in input().split()]

time = 0

# fill in Q's
time += L // M * Q

# remaining Q's
remain = L % M
if remain > 0: time += Q

# fill in 1's
if remain > 0: S -= (M - remain) * Q 

# remaining 1's
if S > 0: time += (S+M-1) // M

print(time)

