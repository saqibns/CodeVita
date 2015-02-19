#include<stdio.h>
int main()
{
    int x, y, z;
    x = y = z = 1;
    x += y += z;
    printf("%d %d %d\n", x, y, z);
    printf("%d\n", z += x < y ? x++ : y++);
    printf("%d %d %d\n", x, y, z);
    return 0;
}
