import sys
sys.stdin = open('input.txt','r')

for i in range(10):
    a = int(input())
    case = list(map(int, input().split()))
    result = 0
    for k in range(4,a):
        if case[k-2] > case[k] and case[k-2] > case[k-1] and case[k-2] >case[k-3] and case[k-2]>case[k-4]:
            b = sorted(case[k-4:k+1])
            result += b[4]-b[3]
            
    print('#{} {}'.format(i+1, result))
    
''' Solution
T = 10
for tc in range(1,T+1):
    N = int(input())
    h = list(map(int, input().split()))
    view = 0
    for i in range(2, N-2):
        # left = h[i-2] if (h[i-2]>h[i-1]) else h[i-1] #삼항연산자
        # right = h[i+2] if (h[i+2]>h[i+1]) else h[i+1]
        # t = left if (left>right) else right
        t = max(h[i-2],h[i-1],h[i+1],h[i+2])

        if(h[i] > t):
            view += (h[i]-t)

print(f'#{tc} {view}')
'''