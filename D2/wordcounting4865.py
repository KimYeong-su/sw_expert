T = int(input())

for tc in range(1,T+1):
    s1 = input()
    s2 = input()

    max = 0
    for i in s1:
        cnt = 0
        for j in s2:
            if i == j:
                cnt += 1
            if max<cnt:
                max=cnt

    print('#{} {}'.format(tc, max))