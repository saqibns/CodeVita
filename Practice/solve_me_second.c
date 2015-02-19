#include<stdio.h>
int main()
{
    int i, lines, first, second;
    scanf("%d", &lines);
    for(i = 0; i < lines; i++)
    {
        scanf("%d %d", &first, &second);
        printf("%d\n", (first + second));
    }
    return 0;
}
