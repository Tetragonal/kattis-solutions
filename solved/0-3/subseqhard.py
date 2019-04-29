TARGET = 47

T = int(input())

for _ in range(T):
    input()
    N = input()
    arr = [int(x) for x in input().split(' ')]

    sums = dict()

    sum = 0
    for idx, val in enumerate(arr):
        sum += val
        if sum not in sums:
            sums[sum] = []
        sums[sum].append(idx)
    # print(sums)
    count = 0
    for val, r_idx_arr in sums.items():
        for r_idx in r_idx_arr:
            if val == TARGET:
                count += 1
            if val - TARGET in sums:
                for l_idx in sums[val - TARGET]:
                    # print(l_idx, r_idx)
                    if l_idx <= r_idx:
                        count += 1
    print(count)
