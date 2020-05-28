T = int(input())
for tc in range(1,T+1):
    # N : 접수창구갯수, M : 정비창구갯수, K : 방문자수
    # A : 지갑 놓고간 접수창구, B : 지갑 놓고간 정비창구
    N, M, K, A, B = map(int,input().split())
    a = list(map(int,input().split()))
    h_a = [[]for _ in range(N)]
    t_a = [0]*N
    b = list(map(int,input().split()))
    h_b = [[]for _ in range(N)]
    t_b = [0]*M
    time = list(map(int,input().split()))
    if time[0]!=0:
        for i in range(K):
            time[i] -= time[0]
    cnt = 0
    temp_a = []
    temp_b = []
    num = 1
    while True:
        # time-> temp_a
        while True:
            if time[0]==cnt:
                time.pop(0)
                temp_a.append(num)
                num += 1
            else:
                break

        # a time count and a->temp_b
        for i in range(N):
            if t_a[i]!=0:
                t_a[i] -= 1
                if t_a[i]==0:
                    temp_b.append(h_a[i][-1])

        # b time count
        for i in range(M):
            if t_b[i]!=0:
                t_b[i] -= 1
                if t_b[i]==0:
                    

        # temp_a -> a
        for i in range(N):
            if t_a[i]==0:
                h_a[i].append(temp_a.pop(0))
                t_a[i]=a[i]
        
        # temp_b -> b
        for i in range(M):
            if t_b[i]==0:
                h_b[i].append(temp_b.pop(0))
                t_b[i]=b[i]
