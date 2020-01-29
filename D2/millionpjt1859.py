cases = int(input())

for case in range(cases):
    d = int(input())
    benefit = list(map(int,input().split()))
    result = 0
    while benefit != []:
        b_sort = list(sorted(benefit))
        k = 0

        n = benefit.index(b_sort[len(b_sort)-1])
        for i in benefit[:n]:
            result -= i
            k += 1
        # print(result)
        result += b_sort[len(b_sort)-1] * k
        benefit = benefit[n+1:]
        # print(benefit)
        # print(result)

    print(f'#{case+1} {result}')

'''
n = int(input())
 
for i in range(n):
    case_num = int(input())
    raw_data = input()
    price_data = list(map(int, raw_data.split()))
    benefit = 0
    last_one = price_data[-1]
    for j in range(1, case_num):
        if price_data[-1-j] <= last_one:
            benefit += last_one - price_data[-1-j]
 
        else:
            last_one = price_data[-1-j]
 
 
    print('#'+str(i+1)+' '+str(benefit))
'''