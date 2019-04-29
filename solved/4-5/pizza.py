test_cases = int(input())

for _ in range(test_cases):
    # Create x_list and y_list
    x, y = [int(x) for x in input().split(' ')]
    x_list = [0]*x
    y_list = [0]*y
    for y_idx in range(y):
        line = [int(x) for x in input().split(' ')]
        for x_idx, num in enumerate(line):
            x_list[x_idx] += num
            y_list[y_idx] += num
    # Find best spot for restaurant
    min_x = float('inf')
    min_y = float('inf')
    for x_idx in range(len(x_list)):
        cost = sum([num * abs(x_idx - idx) for idx, num in enumerate(x_list)])
        min_x = min(min_x, cost)
    for y_idx in range(len(y_list)):
        cost = sum([num * abs(y_idx - idx) for idx, num in enumerate(y_list)])
        min_y = min(min_y, cost)
    print(str(min_x + min_y) + ' blocks')
