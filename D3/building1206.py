for i in range(10):
    a = int(input())
    case = list(map(int, input().split()))
    result = 0
    for k in range(4,a):
        if case[k-2] > case[k] and case[k-2] > case[k-1] and case[k-2] >case[k-3] and case[k-2]>case[k-4]:
            b = sorted(case[k-4:k+1])
            result += b[4]-b[3]
            
    print(f'#{i+1} {result}')
    