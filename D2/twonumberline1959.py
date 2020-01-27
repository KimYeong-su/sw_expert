cases = int(input())

for case in range(cases):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []

    if N<M:
        for k in range(M-N+1):
            result_sum = 0
            for l in range(N):
                result_sum += A[l]*B[k+l]
            result.append(result_sum)

    else:
        for n in range(N-M+1):
            result_sum = 0
            for m in range(M):
                result_sum += A[n+m]*B[m]
            result.append(result_sum)
    
    print(f'#{case+1} {max(result)}')