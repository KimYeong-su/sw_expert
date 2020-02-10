T = int(input())

for tc in range(1,T+1):
    score = list(map(int,input().split()))

    sum = 0
    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40
        sum += score[i]
    result = sum//5
    print('#{} {}'.format(tc,result))