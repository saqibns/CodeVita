#include<stdio.h>
int main()
{
    unsigned long a, b, c, i, n;
    n = 600851475143;
    printf("%ld\n", n);
    n = 13195;
    for(i = 2; i < n; i++)
    {
        if(n % i == 0)
        {
            if(is_prime(i))
                a = i;
        }
    }
    printf("%d", a);
    return 0;
}

int is_prime(long n)
{
    long i;
    for(i = 2; i < n; i++)
    {
        if(n % i == 0)
            return 0;
    }
    return 1;
}

