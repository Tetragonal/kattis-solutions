n = int(input())

word_count = dict()
sentence = [x for x in input().split(' ')]
for word in sentence:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

# print(word_count)
m = int(input())

correct_counts = dict()
total_counts = dict()

dutch_to_eng = dict()

for _ in range(m):
    line = [x for x in input().split(' ')]
    dutch = line[0]
    eng = line[1]
    correct = line[2] == 'correct'
    if dutch not in correct_counts:
        correct_counts[dutch] = 0
        total_counts[dutch] = 0
    if correct:
        correct_counts[dutch] += 1
    total_counts[dutch] += 1
    dutch_to_eng[dutch] = line[1]

# print(correct_counts)
# print(total_counts)
correct_count = 1
for word in correct_counts.keys():
    if word not in word_count:
        word_count[word] = 0
    correct_count *= correct_counts[word] ** word_count[word]

total_count = 1
for word in total_counts.keys():
    total_count *= total_counts[word] ** word_count[word]

incorrect_count = total_count - correct_count

if total_count != 1:
    print(str(correct_count) + ' correct')
    print(str(incorrect_count) + ' incorrect')
else:
    print(' '.join([dutch_to_eng[x] for x in sentence]))
    if correct_count > 0:
        print('correct')
    else:
        print('incorrect')