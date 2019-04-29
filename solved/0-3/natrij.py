day = 24 * 3600

h1, m1, s1 = [int(x) for x in input().split(':')]
h2, m2, s2 = [int(x) for x in input().split(':')]

t1 = h1*3600 + m1 * 60 + s1
t2 = h2*3600 + m2 * 60 + s2

diff = t2 - t1
if diff <= 0: diff += day

print("%02d:%02d:%02d" % (diff//3600, (diff % 3600) // 60, diff%60))


