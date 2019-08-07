import math 
# n is decimal, k is the number of repeating last digits
def solve(n, k):
  #assert int(n) >= k
  n1 = int(n[:k]) if k > 0 else 0
  n2 = int(n[k:])

  nines = int("9"*len(n[k:]))
  a = n1*nines + n2
  b = nines * 10**k
  g = math.gcd(a,b)
  return a//g, b//g

def simplify(a, b):
  g = math.gcd(a,b)
  return a//g,b//g

while True:
  s = input()
  if s == "0": break
  s = s[2:]
  if s[-3:] == '...':
    s = s[:-3]
    repeat = True
  else:
    repeat = False


  b = 10**len(s)
  if repeat:
    choices = [solve(s, i) for i in range(len(s))]
    denominator = min(map(lambda x: x[1], choices))
    a, b = simplify(*list(filter(lambda x: x[1] == denominator, choices))[0])
  else:
    a, b = simplify(int(s),b)
  print("%s/%s" % (a, b))
