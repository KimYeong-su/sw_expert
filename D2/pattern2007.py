# 너무 어렵게 짰는데.. while 대신에 for 문으로 짜면 더 간단함
a = int(input())

for i in range(a):
    b = list(input())
    cnt = 0
    k=1
    while k <30:
        if k>15:
            if b[0:30-k] == b[k:30]:
                cnt = k
                break
        else:
            if b[0:k] == b[k:2*k]:
                cnt = k
                break

        k += 1

    print(f'#{i+1} {k}')