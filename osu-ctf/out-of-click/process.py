solns = []
with open('objs.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        if ' ' in line[0]:
            solns.append(line[0])
            solns.append(line[1])

final = ''

for i in solns:
    a = i.strip().split(' ')
    final += chr(int(a[0]))
    final += chr(int(a[1]))
print(final)