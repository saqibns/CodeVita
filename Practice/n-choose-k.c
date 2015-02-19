#include<stdio.h>
int choose(int, int);
int main()
{
    printf("%d\n", choose(1, 1));
    printf("%d\n", choose(6, 2));
    printf("%d\n", choose(7, 3));
    printf("%d\n", choose(6, 4));
    printf("%d\n", choose(10, 4));
    return 0;
}

int choose(int n, int k)
{
    if(n == k)
        return 1;
    else if(k == 0)
        return 1;
    else if(k == 1)
        return n;
    else
        return choose(n - 1, k - 1) + choose(n - 1, k);
}
