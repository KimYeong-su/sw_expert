cases = int(input())

for case in range(cases):
    N, K = map(int, input().split())
    base = []
    for i in range(N):
        temp = list(map(int,input().split()))
        