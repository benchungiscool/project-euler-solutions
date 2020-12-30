fib = [1, 2, 3]
while True:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] > 4000000:
        fib.pop(-1)
        print(sum([i for i in fib if not i % 2]))
        break