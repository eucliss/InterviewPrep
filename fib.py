import time

# 0 : 0
# 1 : 1
# 2 : 1
# 3 : 2
# 4 : 3
# 5 : 5
# 6 : 8 = 23
# 7 : 13
# 8 : 21 = 3 x 7
# 9 : 34 = 2 x 17
# 10 : 55 = 5 x 11
# 11 : 89
# 12 : 144 = 24 x 32
# 13 : 233
# 14 : 377 = 13 x 29
# 15 : 610 = 2 x 5 x 61
# 16 : 987 = 3 x 7 x 47
# 17 : 1597
# 18 : 2584 = 23 x 17 x 19
# 19 : 4181 = 37 x 113
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fiblist(n):
    dict = {}
    return fib2(n, dict)

def fib2(n, dict):
    if n == 0:
        dict[n] = 0
        return 0
    if n == 1:
        dict[1] = 1
        return 1
    elif n in dict:
        return dict[n]
    else:
        dict[n] = fib2(n-1, dict) + fib2(n-2, dict)
        return dict[n]


if __name__ == '__main__':
    start_time = time.time()
    # print(fib2(0, {}))
    # print(fib2(1, {}))
    # print(fib2(2, {}))
    print(fiblist(200))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    # print(fib2(0, {}))
    # print(fib2(1, {}))
    # print(fib2(2, {}))
    print(fib(36))
    print("--- %s seconds ---" % (time.time() - start_time))
