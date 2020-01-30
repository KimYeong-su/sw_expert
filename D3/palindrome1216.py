# cases = 10

# for case in range(cases):
#     n = int(input())
#     search = 100
#     base = [] # 주어진 배열을 그대로
#     base2 = [] # 주어진 배열의 행과 열을 바꾸기
#     for i in range(100):
#         base.append(list(input()))

#     for i in range(100): #배열의 행과 열 바꾸기
#         temp = []
#         for k in range(100):
#             temp.append(base[k][i])
#         base2.append(temp)

#     while search>1:
#         cnt = 0
#         for i in range(100):
#             for j in range(101-search):
#                 print(j)
#                 if base[i][j:search+j] == list(reversed(base[i][j:search+j])):
#                     print(f'#{case+1} {search}')
#                     break
#                 elif base2[i][j:search+j] == list(reversed(base2[i][j:search+j])):
#                     print(f'#{case+1} {search}')
#                     break
#             search -= 1

cases = 10

for case in range(cases):
    n = int(input())
    search = 100
    base = [] # 주어진 배열을 그대로
    base2 = [] # 주어진 배열의 행과 열을 바꾸기
    for i in range(100):
        base.append(list(input()))

    for i in range(100): #배열의 행과 열 바꾸기
        temp = []
        for k in range(100):
            temp.append(base[k][i])
        base2.append(temp)

    result = 0
    while search>1:
        cnt = 0
        for i in range(100):
            for j in range(101-search):
                if base[i][j:search+j] == list(reversed(base[i][j:search+j])):
                    if result < search:
                        result = search
                
                if base2[i][j:search+j] == list(reversed(base2[i][j:search+j])):
                    if result < search:
                        result = search
        search -= 1

    print(f'#{case+1} {result}')