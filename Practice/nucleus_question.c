#include<stdio.h>
int main()
{
    int i, n, limit, count, print, inc, line;
    count = 0;
    line = 1;
    print = 1;
    inc = 1;
    scanf("%d", &n);
    limit = n * (n + 1) / 2;
    /*printf("limit: %d\n", limit);*/
    for(i = 1; i <= limit; i++)
    {
        printf("%d ", print);
        count++;
        if(count == line)
        {
            line++;
            print = line;
            inc++;
            printf("\n");
            count = 0;
        }
        else
        {
            print += inc;
        }
    }
    return 0;
}
