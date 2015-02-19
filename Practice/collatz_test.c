#include<stdio.h>
int sequence(int);
int main()
{
    printf("%d", sequence(3));
    return 0;
}

int sequence(int n)
{
    if(n == 1)
        return 1;
    else
    {
        if(n % 2 == 0)
            return 1 + sequence(n / 2);
        else
            return 1 + sequence(3 * n + 1);
    }
}
