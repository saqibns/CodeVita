#include<stdio.h>
#include<limits.h>
void print_array(int[], int, int);
int main()
{
    int max, n, start, end, sum;
    n = 16;
    int a[16] = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    int i, j;
    max = INT_MIN;
    for(i = 0; i < n; i++)
    {
        sum = 0;
        for(j = i; j < n; j++)
        {
            sum += a[j];
            if(sum > max)
            {
                start = i;
                end = j;
                max = sum;
                printf("%d %d %d\n", max, start, end);
            }
        }
    }
    printf("%d\n", max);
    print_array(a, start, end);
    return 0;
}

void print_array(int a[], int start, int end)
{
    int i;
    for(i = start; i <= end; i++)
        printf("%d ", a[i]);
    printf("\n");
}
