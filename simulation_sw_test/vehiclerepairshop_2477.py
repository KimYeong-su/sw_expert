import heapq

T = int(input())
for tc in range(1,T+1):
    # N : 접수창구갯수, M : 정비창구갯수, K : 방문자수
    # A : 지갑 놓고간 접수창구, B : 지갑 놓고간 정비창구
    N, M, K, A, B = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    customers = list(map(int,input().split()))
    used_counter = []
    visit_a = [0] * N
    visit_b = [0] * M
    result = 0
    for i, t in enumerate(customers):
        w = 0
        w_idx = 0
        while w < N:
            if visit_a[w] <= t:
                w_idx = w
                break
            if visit_a[w] < visit_a[w_idx]:
                w_idx = w
            w += 1

        visit_a[w_idx] = max(t,visit_a[w_idx]) + a[w_idx]
        customers[i] = [i,visit_a[w_idx], w_idx]
        if w_idx == A-1:
            used_counter.append(i)
    customers = sorted(customers, key=lambda x: (x[1],x[2]))
    for customer in customers:
        num, t, _ = customer
        w = 0
        w_idx = 0
        while w < M:
            if visit_b[w] <= t:
                w_idx = w
                break
            if visit_b[w] < visit_b[w_idx]:
                w_idx = w
            w += 1

        visit_b[w_idx] = max(t, visit_b[w_idx]) + b[w_idx]
        if w_idx == B-1 and num in used_counter:
            result += num + 1
    
    if not result:
        result = -1

    print('#{} {}'.format(tc, result))