# # Solution 2. -> 시간초과
# def check(num, cnt):
#     if cnt in result:
#         return
#     if num == N:
#         return
#     result.append(cnt)
#     for i in range(N):
#         if visit[i]==0:
#             visit[i]=1
#             cnt += base[i]
#             check(num+1,cnt)
#             visit[i]=0
#             cnt -= base[i]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base = list(map(int,input().split()))
    sum = 0
    for i in base:
        sum += i
    visit = [0 for _ in range(sum+1)]
    visit[0] = 1

    for i in base:
        for j in range(sum,-1,-1):
            if visit[j]==1:
                visit[j+i]=1
    result = visit.count(1)
    # # Solution 1. -> 시간초과
    # result = set()
    # for i in range(1<<N):
    #     temp = 0
    #     for j in range(N+1):
    #         if i & (1<<j):
    #             temp += base[j]
    #     result.add(temp)

    
    # result = []
    # check(0,0) # 프린트 할때 한개 더해줘야합니다.
    print('#{} {}'.format(tc,result))