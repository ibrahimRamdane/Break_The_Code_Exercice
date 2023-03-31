file = open('coteBretonne.txt', 'r')
contents = file.readlines()
# print(contents)
chaine = ''
for sentence in contents:
    a = sentence.split()
    chaine = chaine + a[0]
# print(len(chaine))
L = []
b = 0
i = 0
print(len(chaine))
while i < 4977:
    if chaine[i] == 'V':
        for j in range(i, len(chaine)-2):
            if chaine[j+1] != 'V' and chaine[j+2] != 'V':
                if i == 0:
                    L.append(chaine[i:j+2])
                else:
                    L.append(chaine[i-1:j+2])
                i = j+2
                break

    else:
        i = i+1
print(L)
max_value = None
P = []

for x in L:
    p = 0
    for y in x:
        if y == 'V':
            p = p+1
    P.append(p)
print(P)

l = 0
for x in P:
    if (max_value is None or x > max_value and 'D' not in L[l] and 'F' in L[l]):
        max_value = x
        m = l
    l = l+1

print(m)
#print(list, max_value)
# print(L.index('MVFVMVVVMVMVVVFVFVM'))
