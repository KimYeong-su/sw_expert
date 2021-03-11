T = int(input())
for tc in range(1, T+1):
    P = int(input())
    base = list(map(int, input().split()))
    print(f'#{tc} {max(base)*min(base)}')