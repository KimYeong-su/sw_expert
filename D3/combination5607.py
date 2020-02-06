cases = int(input())

for case in range(cases):
    N, R = map(int,input().split())
    result = 1
    for i in range(N,N-R,-1):
        result = result * i
    for k in range(2,R+1):
        result = result / k
    print('#{} {}'.format(case+1,int(result)))