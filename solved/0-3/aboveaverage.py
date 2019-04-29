C = int(input())

for _ in range(C):
    arr = [float(x) for x in input().split()][1:]
    avg = sum(arr) / len(arr)
    total = 0.
    for elm in arr:
        if elm > avg:
            total += 1
    print(str('%.3f' % (100*total / len(arr))) + '%')
