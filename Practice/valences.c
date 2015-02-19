#include<stdio.h>
int find(int);
int main()
{
    int start;
    scanf("%d", &start);
    while(start != 0)
    {
        //printf("%d\n", start);
        printf("%d\n", find(start));
        scanf("%d", &start);
    }
    return 0;
}

int find(int n)
{
    int i, tmp, sum, pos;
    pos = (n >> 1) + 1;
    //printf("pos: %d\n", pos);
    sum = 0;
    for(i = 1; i <= n; i++)
    {
        //printf("i: %d\n", i);
        scanf("%d", &tmp);
        if(i >= pos)
            sum += tmp;
    }
    return sum;
}

