cases = int(input())

for case in range(cases):

    N, M = map(int,input().split())

    fly_num = []
    catch_num = []
    init_range = N-M+1

    for i in range(N):
        fly_num.append(list(map(int,input().split())))

    for l in range(init_range):
        for o in range(init_range):
            cnt = 0
            for j in range(M):
                for k in range(M):
                    cnt += fly_num[l+j][o+k]
            catch_num.append(cnt)

    print(f'#{case+1} {max(catch_num)}')