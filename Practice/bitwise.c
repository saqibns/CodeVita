#include<stdio.h>
int count(int);
int main()
{
    printf("%d", count(16));
    return 0;
}

int count(int n)
{
    int x = 0;
    while(n != 0)
    {
        if(n & 01)
            x++;
        n >>= 1;
    }
    return x;
}
