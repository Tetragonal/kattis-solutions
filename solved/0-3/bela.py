d = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
d2 = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}


N, B = [x for x in input().split()]
N = int(N)

tot = 0
for _ in range(4*N):
  char, suit = [x for x in input()]
  if suit == B: tot += d[char]
  else: tot += d2[char]
print(tot) 
