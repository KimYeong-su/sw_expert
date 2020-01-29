cases = int(input())

for case in range(cases):
    base = list(sorted(map(int, input().split())))
    base.remove(base[0])
    base.remove(base[len(base)-1])
    sum = 0
    for i in base:
        sum += i
    avg = round(sum/len(base))
    print(f'#{case+1} {avg}')