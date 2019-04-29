N = int(input())

total = 0
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
arr.reverse()
for i in range(N):
    if i % 3 == 2:
        total += arr[i-2] + arr[i-1]
if len(arr) % 3 == 1:
    total += arr[-1]
elif len(arr) % 3 == 2:
    total += arr[-1] + arr[-2]
print(total)