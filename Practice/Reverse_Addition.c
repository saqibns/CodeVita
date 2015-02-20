#include<stdio.h>

int reverse(int);

int main()
{
    int i, first, second, test_cases;
    scanf("%d", &test_cases);
    for(i = 1; i <= test_cases; i++)
    {
        scanf("%d %d", &first, &second);
        printf("%d\n", reverse(reverse(first) + reverse(second)));
    }
    //scanf("%d", &n);
//    printf("%d", reverse(n));
    
    //getch();
    return 0;
}

int reverse(int n)
{
    int reversed = 0;
    while(n > 0)
    {
        reversed = 10 * reversed + (n % 10);
        n /= 10;
    }
    return reversed;
}
