#lambda and map() functions...
cube = lambda x: x**3 

def fibonacci(n):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    fibon = []

    # if there is only one term, return n1
    if n == 1:
        fibon.append(0)
        # generate fibonacci sequence
    else:
        while count < n:
            fibon.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    return fibon

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
