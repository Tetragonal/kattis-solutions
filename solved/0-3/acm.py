penalty = 0
score = 0
problem = dict()
while True:
    line = input()
    if line == '-1':
        break
    time, name, correct = [x for x in line.split()]
    if correct == 'right':
        if name not in problem:
            problem[name] = 0
        penalty += int(time) + problem[name]
        score += 1
    else:
        if name not in problem:
            problem[name] = 0
        problem[name] += 20
print(score, penalty)
