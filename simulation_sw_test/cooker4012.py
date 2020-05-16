def f(n,k,s,e):
    global minimum
    if n==k:
        temp = 0
        for a in range(N):
            for b in range(N):
                if a!=b:
                    if (a in C) and (b in C):
                        temp += table[a][b]
                    elif (a not in C) and (b not in C):
                        temp -= table[a][b]
        if minimum>abs(temp):
            minimum = abs(temp)
        return
    else:
        for i in range(s, e-k+n+1):
            C[n] = i
            f(n+1,k,i+1,e)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split()))for _ in range(N)]
    minimum = 20000
    C = [0]*(N//2)
    f(0,N//2,0,N)
 

    print('#{} {}'.format(tc,minimum))