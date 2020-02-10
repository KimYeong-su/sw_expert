T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    for unicorn in range(M+1):
        for twinhorn in range(M,-1,-1):
            if N == unicorn + twinhorn*2:
                if M == unicorn + twinhorn:
                    if unicorn >= 0 and twinhorn>= 0:
                        print('#{} {} {}'.format(tc,unicorn,twinhorn))