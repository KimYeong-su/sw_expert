def search(start):
    global answer
    if start == 99:
        answer = 1
        return
    if answer==1:
        return
    if arr1[start] != -1:
        search(arr1[start])
    if arr2[start] != -1:
        search(arr2[start])

while True:
    try:
        tc, N = map(int, input().split())
    except:
        break
    base = list(map(int, input().split()))
    arr1 = [-1] * 100
    arr2 = [-1] * 100
    for i in range(N):
        if arr1[base[i*2]] != -1:
            arr2[base[i*2]] = base[i*2 + 1]
        else:
            arr1[base[i*2]] = base[i*2 + 1]
    answer = 0
    search(0)
    print(f'#{tc} {answer}')