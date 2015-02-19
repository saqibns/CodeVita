#include<stdio.h>
int main()
{
//    int a, b, c;
//    int x;
//    char string[10];
//    x = scanf("%d%d%s%d", &a, &b, string, c);
//    printf("%d\n", x);
    char string[10];
    int i = 0;
    while(scanf("%s", string) == 1)
          i++;
    printf("%d", i);
    return 0;
}
