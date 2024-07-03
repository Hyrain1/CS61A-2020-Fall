#Q1.1
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp<60 :
        return True
    elif raining: 
        return True
    else : 
        return False
        
def wears_jacket(temp,raining):
    """
    >>> wears_jacket(90,False)
    False
    >>> wears_jacket(40,False)
    True
    >>> wears_jacket(100,True)
    True
    """
    return temp<60 or raining

#Q1.2 Infinite loop

#Q1.3
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i=2
    while i*i<=n :
        if n%i==0:
            return False
        i+=1
    return True