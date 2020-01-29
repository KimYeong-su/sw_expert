cases = 10

for case in range(cases):
    n = int(input())
    search = input()
    S = input()

    cnt = 0
    for i in range(len(S)-len(search)+1):
        if S[i:i+len(search)] == search:
            cnt += 1

    print(f'#{n} {cnt}')