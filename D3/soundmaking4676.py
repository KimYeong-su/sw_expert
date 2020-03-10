T = int(input())

for tc in range(1,T+1):
    s = input()
    H = int(input())
    
    place = list(sorted(map(int,input().split()),reverse=True))

    for i in place:
        s = s[:i]+'-'+s[i:]
    
    print('#{} {}'.format(tc,s))