#1.1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n==1 :
        return m
    return m+multiply(m,n-1)
#1.3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n==1:
        return 1
    else :
        if n%2==0:
            return 1 + hailstone(n//2)
        else :
            return 1 + hailstone(n*3+1)
#1.4
def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1==0 or n2==0 :
        return n1+n2
    else :
        last1,last2=n1%10,n2%10
        if last1<last2 :
            return merge(n1//10,n2)*10+last1
        else :
            return merge(n1,n2//10)*10+last2
#1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(t):
        if t==1:
            return f(x)
        else:
            return f(repeat(t-1))
    return repeat
#1.6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(k):
        if k>=n:
            return True
        elif n%k==0:
            return False
        else:
            return prime_helper(k+1)
    if n==1 :
        return False
    return prime_helper(2)