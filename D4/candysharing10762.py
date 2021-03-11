T = int(input())

for tc in range(1,T+1):
    N = int(input())
    candies = list(map(int, input().split()))
    a, b = 0, 0
    answer = "NO"
    for i in candies:
        a += i
        b ^= i
    if not b:
        answer = a - min(candies)
    print(f'#{tc} {answer}')