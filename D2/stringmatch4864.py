T = int(input())

for tc in range(1,T+1):
    s1 = input()
    s2 = input()

    for i in range(len(s2)):
        if s1==s2[i:i+len(s1)]:
            print('#{} 1'.format(tc))
            break
        if i == len(s2)-1:
            print('#{} 0'.format(tc))