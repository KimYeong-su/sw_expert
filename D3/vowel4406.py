T = int(input())

for tc in range(1,T+1):
    s = input()
    vowel = ['a','e','i','o','u']
    result = ''
    for i in s:
        if i not in vowel:
            result += i
    print('#{} {}'.format(tc,result))