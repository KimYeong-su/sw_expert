cases = int(input())

for case in range(cases):
    cnt = []
    num = []
    if case == int(input())-1:
        num = list(map(int,input().split()))    
        for i in range(101):
            cnt.append(num.count(i))
        r_cnt = list(reversed(cnt))
        print(f'#{case+1} {100-r_cnt.index(max(cnt))}')