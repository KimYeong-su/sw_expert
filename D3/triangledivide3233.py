T = int(input())

for tc in range(1,T+1):
    A, B = map(int,input().split())
    result = 0
    for i in range(1,A//B+1):
        result += 2*i-1

    print('#{} {}'.format(tc,result))