cases = int(input())

for case in range(cases):
    N, K = map(int, input().split())
    base = []
    for i in range(N):
        temp = list(map(int,input().split()))
        base.append(temp)

    result = 0
    for i in range(N):
        cnt = 0
        stack = []
        for j in range(N):
            if base[i][j] == 1:
                cnt += 1
                if j == N-1:
                    stack.append(cnt)
            else:
                stack.append(cnt)
                cnt = 0
        result += stack.count(K)

            

    for j in range(N):
        cnt = 0
        stack = []
        for i in range(N):
            if base[i][j] == 1:
                cnt += 1
                if i == N-1:
                    stack.append(cnt)
            else:
                stack.append(cnt)
                cnt = 0
        result += stack.count(K)


    print(f'#{case+1} {result}')