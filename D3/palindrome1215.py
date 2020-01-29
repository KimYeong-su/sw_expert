cases = 10

for case in range(cases):
    search = int(input())
    base = []
    for i in range(8):
        base.append(list(input()))

    for i in range(8):
        for j in range(len(base)-search+1):
            for k in range(search):
                