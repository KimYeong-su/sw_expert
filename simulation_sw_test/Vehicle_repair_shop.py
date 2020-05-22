T = int(input())
for tc in range(1,T+1):
    # N : 접수창구갯수, M : 정비창구갯수, K : 방문자수
    # A : 지갑 놓고간 접수창구, B : 지갑 놓고간 정비창구
    N, M, K, A, B = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    time = list(map(int,input().split()))
    