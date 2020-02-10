T = int(input())

for tc in range(1,T+1):
    a,b,c = map(int,input().split())
    if a==b!=c:
        print('#{} {}'.format(tc,c))
    elif a==c!=b:
        print('#{} {}'.format(tc,b))
    elif b==c!=a:
        print('#{} {}'.format(tc,a))
    elif a==b==c:
        print('#{} {}'.format(tc,a))