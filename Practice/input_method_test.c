#include<stdio.h>
int main()
{
    int n, k, i, integer, count = 0;
    scanf("%d %d", &n, &k);
    for(i = 1; i <= n; i++)
    {
        scanf("%d", &integer);
        if(integer % k == 0)
            count++;
    }
    printf("%d", count);
    //getch();
    return 0;
}
