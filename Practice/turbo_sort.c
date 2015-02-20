#include<stdio.h>

int main()
{
    int tests, i, j, key;
    // Get the number of test cases
    scanf("%d", &tests);
    //printf("%d", tests);
    
    int numbers[tests];
    for(i = 0; i < tests; i++)
    {
        scanf("%d", &numbers[i]);
        key = numbers[i];
        j = i - 1;
        while(numbers[j] > key && j >= 0)
        {
            numbers[j + 1] = numbers[j];
            j--;
        }
        
        numbers[j + 1] = key;
    }
    
    for(i = 0; i < tests; i++)
    {
        printf("%d\n", numbers[i]);
    }
    
    
    //getch();
    return 0;
}
