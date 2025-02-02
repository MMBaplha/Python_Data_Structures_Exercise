def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    i = 1
    
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            if i != num // i: # to avoid duplicates.
                factors.append(num // i)
        i += 1
    
    return sorted(factors)