T = int(input())

for tc in range(1,T+1):
    s = input()
    s = s.lower()

    flag = 1
    for i in range(len(s)):
        if s[i] == '?' or s[-i-1] == '?':
            continue
        if s[i] != s[-i-1]:
            flag = 0
            break
    if flag==1:
        print('#{} Exist'.format(tc))
    else:
        print('#{} Not exist'.format(tc))