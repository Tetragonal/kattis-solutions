input()
arr = list(filter(lambda x: x>=0, map(int, input().split())))
print(sum(arr)/len(arr))
