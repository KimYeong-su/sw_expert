cases = 10

for case in range(cases):
    c = int(input())
    base = list(map(int, input().split()))

    i = 1
    while True:
        temp = base[0]
        temp -= i
        if temp<0:
            break
        base.remove(base[0])
        base.append(temp)
        i += 1

    i = 1
    while base[7] != 0:
        temp = base[0]
        temp -= i
        if temp<0:
            temp = 0
        base.remove(base[0])
        base.append(temp)
        i += 1
    
    a = ' '.join(list(map(str,base)))
    print(f'#{c} {a}')