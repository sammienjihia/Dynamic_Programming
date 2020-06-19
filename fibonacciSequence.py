
"""
Given the first 3 digits in the finacci sequence, to calculate the 
4 digit in the sequence find the 3rd digit in the sequence f(4-1) and 
sum it with the 2nd digit in the sequence f(4-2).

The Nth fibonacci number in the sequence is the summation of 
the (Nth-1) number in the sequence and the (Nth -2) number in the sequence

"""

def computeFibonacci(k):

    # The first 3 digits in the fibonacci sequence are 1, 1, 2

    # without memoization the time complexity of this function shall be O(2^k)

    # reason
    """
                        fib(n)
                      /      \
                     /        \   
                    /          \
                   /            \
                fib(n-1)      fib(n-2)
    To find the fib(n) we shall have to find the fib(n-1) and the fib(n-2) with a time complexity of O(2^n)
    """

    if k == 1 or k == 2:
        return 1

    if k == 3:
        return 2

    return computeFibonacci(k-2) + computeFibonacci(k-1)


# Memoized soulution

cache = {}

def fib(n):
    # To prevent the re-computation of already computed digits in the sequnce, we store the fib(n) in a cache

    # first check if the fib of n is already in the memo array
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1

    if n == 3:
        return 2

    result = fib(n-1) + fib(n-2)

    cache[n] = result

    return result


if __name__ == "__main__":
    k = 35
    n = 400
    print(fib(n))
    print(computeFibonacci(k))
                
