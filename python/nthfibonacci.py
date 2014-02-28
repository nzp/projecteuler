def nth_fibonacci(n):
    fib_list = []

    i = 0
    while i <= n:
        if i == 0 or i == 1:
            fib_list.append(i)
            i += 1 
        else:
            result = fib_list[-2] + fib_list[-1]
            fib_list.append(result)
            i += 1

    return fib_list[-1]

