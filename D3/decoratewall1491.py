T = int(input())

for tc in range(1,T+1):
    N, A, B = map(int, input().split())

    mini = (N-1)*B
    for r in range(1,N+1):
        for c in range(1,N//r+1):
            result = A*abs(r-c)+B*(N-r*c)
            if mini>result:
                mini = result

    print('#{} {}'.format(tc,mini))