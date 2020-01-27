cases = int(input())
date_dic = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}

for case in range(cases):
    d_day = 0
    month1, day1, month2, day2 = map(str, input().split())
    if month1 == month2:
        d_day = int(day2)-int(day1)+1
    else:
        for i in range(int(month1),int(month2)):
            d_day += date_dic[str(i)]
        d_day = d_day + int(day2) - int(day1) +1
    
    print(f'#{case+1} {d_day}')