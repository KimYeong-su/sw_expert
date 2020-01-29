cases = int(input())

for case in range(cases):
    N, K = map(int, input().split())
    base = []
    for i in range(N):
        a, b, c = map(int,input().split())
        temp = 0.35*a + 0.45*b + 0.2*c
        base.append(temp)
    
    base_sort = list(sorted(base))
    # print(base[K-1])
    # print(base_sort.index(base[K-1]))

    if 9*N/10 <= base_sort.index(base[K-1]) < N:
        print(f'#{case+1} A+')
    elif 8*N/10 <= base_sort.index(base[K-1]) < 9*N/10:
        print(f'#{case+1} A0')
    elif 7*N/10 <= base_sort.index(base[K-1]) < 8*N/10:
        print(f'#{case+1} A-')
    elif 6*N/10 <= base_sort.index(base[K-1]) < 7*N/10:
        print(f'#{case+1} B+')
    elif 5*N/10 <= base_sort.index(base[K-1]) < 6*N/10:
        print(f'#{case+1} B0')
    elif 4*N/10 <= base_sort.index(base[K-1]) < 5*N/10:
        print(f'#{case+1} B-')
    elif 3*N/10 <= base_sort.index(base[K-1]) < 4*N/10:
        print(f'#{case+1} C+')
    elif 2*N/10 <= base_sort.index(base[K-1]) < 3*N/10:
        print(f'#{case+1} C0')
    elif N/10 <= base_sort.index(base[K-1]) < 2*N/10:
        print(f'#{case+1} C-')
    else:
        print(f'#{case+1} D0')