cases = int(input())

for case in range(cases):
    number = {'ZRO':0,'ONE':0,'TWO':0,'THR':0,'FOR':0,'FIV':0,'SIX':0,'SVN':0,'EGT':0,'NIN':0}
    s, l = map(str, input().split())
    base = list(map(str, input().split()))

    for i in number:
        c = 0
        c = base.count(i)
        number.values(i) = c
    print(number)


# for case in range(cases):
#     number = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
#     s, l = map(str, input().split())
#     base = list(map(str, input().split()))

#     for i in range(int(l)-2,0,-1):
#         for j in range(i):
#             if number[base[j]] > number[base[j+1]]:
#                 base[j], base[j+1] = base[j+1], base[j]

#     print(s)
#     print(' '.join(base))