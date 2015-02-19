#include<stdio.h>
int main()
{
    int n, max;
    max = 1;
    n = 113383;
    while(n > 1)
    {
        if(n % 2 == 1)
            n = 3 * n + 1;
        else
            n /= 2;
        if(n > max)
            max = n;

            printf("%d\n",n);
    }

    printf("%d", max);

}
