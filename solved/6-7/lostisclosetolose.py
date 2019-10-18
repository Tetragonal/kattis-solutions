import sys
import string

words = []
for line in sys.stdin:
  alp_set = set(string.ascii_lowercase)
  alp = string.ascii_lowercase
  line = line[:-1]
  if line == '': continue
  if line == '***': break
  words += [''.join([y for y in x.lower() if y in alp_set]) for x in line.split()]

words = set(words)
if '' in words: words.remove('')

def sim(word):
  ans = set()
  # del
  for i in range(len(word)):
    ans.add(word[:i] + word[i+1:])
  # add
  for i in range(len(word)+1):
    for c in alp:
      ans.add(word[:i] + c + word[i:])
  # replace
  for i in range(len(word)):
    for c in alp:
      ans.add(word[:i] + c + word[i+1:])
  # transpose
  for i in range(len(word)-1):
      ans.add(word[:i] + word[i+1] + word[i]  + word[i+2:])
  if '' in ans: ans.remove('')
  return ans
d = dict()

for w in words:
  sims = sim(w)
  d[w] = [w2 for w2 in words if w2 in sims and w2 != w]

flag = False
for k,v in sorted(d.items(), key=lambda x: x[0]):
  if len(v) == 0: continue
  print('%s: %s' % (k, ' '.join(sorted(v))))
  flag = True
if not flag:
  print('***')
