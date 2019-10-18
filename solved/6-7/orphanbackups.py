import sys

image = []
backup = []
flag = False
for line in sys.stdin:
  if line == '\n': 
    flag = True
    continue
  if not flag:
    image.append(line[:-1])
  else:
    backup.append(line[:-1])

images = set(image)
backups = set()

ans_image = []
ans_backup = []

for x in backup:
  x2 = x[:x.rfind('_')]
  x2 = x2[:x2.rfind('_')]
  backups.add(x2)
  if x2 not in images:
    ans_backup.append(x)

for x in image:
  if x not in backups:
    ans_image.append(x)

print('\n'.join("F %s" % x for x in sorted(ans_backup)))
print('\n'.join("I %s" % x for x in sorted(ans_image)))

if len(ans_backup) == 0 and len(ans_image) == 0:
  print('No mismatches.')
