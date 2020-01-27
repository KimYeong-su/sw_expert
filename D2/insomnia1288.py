cases = int(input())

for case in range(cases):
    N = int(input())
    result = []
    n = 1
    while True:
        for i in str(N*n):
            result.append(int(i))
        result = sorted(list(set(result)))
        
        if result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
        else:
            n += 1

    print(f'#{case+1} {N*n}')