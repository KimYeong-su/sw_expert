def expo(number, Many):
    if Many == 1:
        return number
    return number*expo(number,Many-1)

cases = 10

for case in range(cases):
    n = int(input())
    num, m = map(int, input().split())
    result = expo(num, m)
    print(f'#{case+1} {result}')
