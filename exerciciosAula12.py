def fatorial(n):
    result = 0
    while n >= 0:
        result = result + (n*(n-1))
        print(result)
        n = n-1
    return result
