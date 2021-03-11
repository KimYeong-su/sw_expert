import heapq

tc = 1
while True:
    try:
        N,start = map(int, input().split())
    except: 
        break
    base = list(map(int, input().split()))
    arr = [[0 for _ in range(101)]for _ in range(101)]
    for i in range(0,N,2):
        arr[base[i]][base[i+1]] = 1
    queue = []
    heapq.heappush(queue,(0,start))
    visit = [False] * 101

    turn, answer = 0, start
    while queue:
        t, s = heapq.heappop(queue)
        flag = False
        for i in range(1,101):
            if arr[s][i] and visit[i]==False:
                visit[i] = True
                heapq.heappush(queue,(t+1, i))
                flag = True
        if flag: continue
        if turn < t:
            turn = t
            answer = s
        elif turn == t:
            if answer < s:
                answer = s

    print(f'#{tc} {answer}')
    tc += 1
