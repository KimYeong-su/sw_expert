case = int(input())

for i in range(case):
    length = int(input())
    result = list(map(int,input().split()))
    print(f'#{i+1} {" ".join(map(str,sorted(result)))}')