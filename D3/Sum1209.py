cases = 10

for case in range(cases):
    n = int(input())
    base = []

    for i in range(100):
        base.append(list(map(int, input().split())))
    
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += base[i][j]
        if i == 0:
            Max = sum
        
        if Max<sum:
            Max = sum

    for j in range(100):
        sum = 0
        for i in range(100):
            sum += base[i][j]
        if Max<sum:
            Max = sum

    for i in range(100):
        sum = 0
        sum += base[i][i]
        if Max<sum:
            Max=sum

    for i in range(100):
        sum = 0
        sum += base[i][99-i]
        if Max<sum:
            Max = sum

    print(f'#{case+1} {Max}')