from sys import stdin

arr = [x.strip() for x in stdin]

defs = {}
defs_inv = {}

for line in arr:
    split = line.split(' ')
    cmd = split[0]
    split = split[1:]

    if cmd == 'clear':
        defs = {}
        defs_inv = {}
    elif cmd == 'def':
        if split[0] in defs:
            del defs_inv[defs[split[0]]]
        defs[split[0]] = int(split[1])
        defs_inv[int(split[1])] = split[0]
    elif cmd == 'calc':
        total = 0
        add = True
        try:
            for idx, word in enumerate(split):
                if idx % 2 == 0:
                    total += defs[word] * (1 if add else -1)
                else:
                    add = word == '+'
            total = defs_inv[total]
        except:
            total = 'unknown'
        print(' '.join(split) + ' ' + str(total))
"""
for k, v in defs.items():
    print('a', k, v)
for k, v in defs_inv.items():
    print('b', k, v)
"""