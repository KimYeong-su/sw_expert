cases = 10

for case in range(cases):
    c = int(input())
    base = list(map(int, input().split()))

    while base[7] != 0:
        for i in range(1,6):
            temp = base[0]
            temp -= i
            if temp < 0:
                temp = 0
            if base[7] == 0:
                continue
            base.remove(base[0])
            base.append(temp)
    
    a = ' '.join(list(map(str,base)))
    print(f'#{c} {a}')