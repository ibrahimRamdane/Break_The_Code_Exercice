file = open('Exo 1  Mastermind.txt','r')
contents = file.readlines()

for j in range(14):
    L=[]
    for lettre in contents[0]:
        n = 0
        for sentence in contents[2:]:

            if lettre == sentence[j] and int(sentence[15])==1:
                n=n+1
        L.append(n)

    p= max(L)

    d = L.index(p)

    print(contents[0][d])
