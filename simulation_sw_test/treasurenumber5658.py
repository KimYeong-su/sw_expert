T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    num_l = N//4
    base = list(input())*2
    
    result = set()
    for i in range(N):
        for j in range(i,i+N-num_l+1):
            result.add(int(''.join(base[j:j+num_l]),16))
    
    result = list(sorted(result,reverse=True))
    print("#{} {}".format(tc,result[K-1]))