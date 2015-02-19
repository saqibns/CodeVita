#include<stdio.h>
void sort(int[], int, int);
int main()
{
    int i, n;
    n = 2;
    int a[] = {7, 4};
    sort(a, a[n - 1], n);
    for(i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}

void sort(int a[], int element, int length)
{
    int i;
    if(length == 1)
    {
        a[0] = element;
    }

    else
    {
        sort(a, a[length], length - 1);
        i = length - 1;
        while(i >= 0 && a[i] > element)
        {
            a[i + 1] = a[i];
            i--;
        }
        a[i + 1] = element;
    }
}
