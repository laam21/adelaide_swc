def factorial(n):
    ''' Return the factorial of n, an integer >=0
        >>>
    '''
    import math
    if not n>= 0:
        raise ValueError('n must be >= 0')
    if math.floor(n) !=n:
        raise ValueError('n must be integer')
    result = 1
    result = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name == '__main__':
    import doctest
    doctest.testmod()

