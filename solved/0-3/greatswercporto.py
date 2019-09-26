import itertools
from collections import Counter

N = int(raw_input())
words = [raw_input() for _ in range(N)]

forbid_zero = set(w[0] for w in words)

chars = set()
for w in words:
  for c in w: 
    chars.add(c)
char_l = list(chars)

target = words[-1]
words = words[:-1]

def sum_char(s,t):
  return int(''.join('1' if x==t else '0' for x in s))

word_d = Counter()
target_d = Counter()
for c in chars:
  for w in words:
    word_d[c] += sum_char(w,c)
  target_d[c] = sum_char(target,c)

cnt = 0

used = [False] * 10
word_tot = 0
target_tot = 0

def rec(idx):
  global word_tot, target_tot, cnt
  if idx == len(chars):
    if word_tot == target_tot: 
      cnt += 1
  else:
    for i in range(10):
      if used[i]: continue
      curr = char_l[idx]
      if i == 0 and curr in forbid_zero: continue
      used[i] = True
      word_tot += word_d[curr] * i
      target_tot += target_d[curr] * i
      rec(idx+1)
      used[i] = False
      word_tot -= word_d[curr] * i
      target_tot -= target_d[curr] * i
rec(0)
print(cnt)  
