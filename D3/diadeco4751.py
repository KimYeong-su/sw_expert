cases = int(input())
for case in range(cases):
    s = list(input())
    n = len(s)
    first = ['.#.'for i in range(n)]
    second = ['#' for i in range(2*n)]

    print('.'+'.'.join(first)+'.')
    print('.'+'.'.join(second)+'.')
    print('#.'+'.#.'.join(s)+'.#')
    print('.'+'.'.join(second)+'.')
    print('.'+'.'.join(first)+'.')