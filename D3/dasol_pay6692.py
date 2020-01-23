a = int(input())


for i in range(a):
    b = int(input())
    mean = 0
    for k in range(b):
        pi, money = map(float, input().split())
        mean += (pi * money)
    print('#{0} {1:.6f}'.format(i+1,mean))