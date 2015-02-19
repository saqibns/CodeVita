#include<stdio.h>
int main()
{
    int a[4] = {1, 2, 3, 4};
    int *p, (*P)[4];
    P = a;
    p = a;

    printf("%d\n", a);
    printf("%d\n", P);
    printf("%d\n", *P);
    printf("%d\n", **P);
    printf("%d\n", P[1]);
    printf("%d\n\n", &P);
    printf("%d\n", p);
    printf("%d\n", *p);
    printf("%d\n", &p);
    return 0;
}
