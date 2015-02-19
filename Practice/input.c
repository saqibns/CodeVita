#include<stdio.h>
int main()
{
    int i, j, k, l;
    i = j = k = 100;
    scanf("%d%c", &i, &l);
    scanf("%d%d", &j, &k);
    printf("%d\n", i);
    printf("%c %d\n", j, k);
    return 0;
}
