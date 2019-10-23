input = raw_input

MOD = 1000000007

seq = input()
ones = 0
qs = 0

qexp = 1
qexp_prev = 0

cnt = 0
for x in seq:
  if x == '1':
    ones += 1
  elif x == '0':
    cnt += qexp * ones + (qexp_prev * qs)
  else:
    cnt += cnt + qexp * ones + (qexp_prev * qs)
    qs += 1
    qexp_prev = qexp
    qexp = (qexp*2)%MOD
  cnt %= MOD
print(cnt)
