#include<stdio.h>
#include<math.h>

// Second attempt at making an efficient prime number generator

int main()
{
    int test_cases, i, lower_lim, upper_lim, j;
    // Get the number of test cases
    scanf("%d", &test_cases);
    //printf("%d", test_cases);
    
    // For every test case, do the following
    for(i = 1; i <= test_cases; i++)
    {
        // Scan the limits
        scanf("%d %d", &lower_lim, &upper_lim);
        // Generate an array containing the numbers from the given limits
        int prime_list[upper_lim - lower_lim];
        
        // Leave a blank line for the next test case
        printf("\n");
        
    }
}
