T = int(input())

for tc in range(1,T+1):
    N = int(input())

    people = [tuple(map(int,input().split()))for _ in range(N)]
    for i in range(N):
        a,b = people[i]
        if a % 2 == 1:
            a = a//2
        else:
            a = a//2-1
        if b % 2 == 1:
            b = b//2
        else:
            b = b//2-1
        if a > b:
            a,b = b,a
        people[i] = (a,b)
    path = [0 for _ in range(200)]
    for i in range(N):
        s,a = people[i]
        for v in range(s,a+1):
            path[v] += 1
    
    print('#{} {}'.format(tc,max(path)))