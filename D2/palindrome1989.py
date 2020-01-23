case = int(input())

for i in range(case):
    sentence = list(input())
    r_sentence = list(reversed(sentence))
    if sentence == r_sentence:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
