n = int(input())

for _ in range(n):
    input()
    input()
    G = max([int(x) for x in input().split()])
    M = max([int(x) for x in input().split()])

    if G < M:
        print('MechaGodzilla')
    else:
        print('Godzilla')