T = int(input())

for tc in range(1,T+1):
    N = int(input())

    prime = [2]
    for i in range(2,N):
        for j in range(2,i):
            if i%j==0:
                break
            if j==i-1:
                prime.append(i)

    cnt=0
    for a in range(len(prime)-2):
        for b in range(a,len(prime)-1):
            for c in range(b,len(prime)):
                if N == prime[a]+prime[b]+prime[c]:
                    cnt+=1
    print('#{} {}'.format(tc,cnt))