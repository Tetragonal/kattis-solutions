import collections
cnt = collections.Counter(list(input()))
t,c,g = cnt['T'], cnt['C'], cnt['G']
print(t*t+c*c+g*g + 7*min(t,c,g))
