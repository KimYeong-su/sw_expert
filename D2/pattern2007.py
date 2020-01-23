a = int(input())

for i in range(a):
    b = list(input())
    c = set(b)
    cnt = 0
    for k in c:
        if b.count(k):
            cnt += 1
    print(cnt)