d = int(input())
for _ in range(d):
    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr2 = []
    tmp = []
    for elem in arr:
        if elem == m:
            arr2.append(tmp)
            tmp = []
        else:
            tmp.append(elem)
    arr2.append(tmp)
    best = m
    for i in range(1,len(arr2)):
        total = m
        arr2[i - 1].reverse()
        for elem in arr2[i-1]:
            if elem < m:
                break
            else:
                total += elem
        arr2[i - 1].reverse()
        for elem in arr2[i]:
            if elem < m:
                break
            total += elem
        if total > best:
            best = total
    print(best)
