n = int(input())

for _ in range(n):
    a, b, c, d = [int(x) for x in input().split(' ')]
    arr = [a, b, c]
    arr.sort()

    if d >= 100:
        print(arr[0]**2 + arr[1]**2 + (arr[2]+d)**2 + 7*arr[0])
    else:
        max_ans = a**2 + b**2 + c**2 + 7*min(a,b,c)
        for i in range(d+1):
            for i2 in range(d+1-i):
                i3 = d-i-i2

                a_tmp = a + i
                b_tmp = b + i2
                c_tmp = c + i3

                max_ans = max(max_ans, a_tmp**2 + b_tmp**2 + c_tmp**2 + 7*min(a_tmp,b_tmp,c_tmp))
        print(max_ans)


