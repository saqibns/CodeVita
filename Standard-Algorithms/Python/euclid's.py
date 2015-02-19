def gcd(m, n):
    """
    Computes Greatest Common Divisor aka Highest Common Factor of two natural
    numbers.

    Accepts: Two natural numbers 'm' and 'n'

    Returns: GCD (HCF)
    """
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

###Tests:
##print gcd(10, 5)
##print gcd(10, 6)
##print gcd(2, 3)