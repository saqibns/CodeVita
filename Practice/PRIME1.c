#include<stdio.h>
#include<math.h>
int isPrime(int);

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
        //printf("%d %d\n", lower_lim, upper_lim);
        
        // Generate all the numbers between the limits, perform a primality test
        for(j = lower_lim; j <= upper_lim; j++)
        {
            if(isPrime(j) == 1)
                printf("%d\n", j);
        }
        // Leave a blank line for the next test case
        printf("\n");
        
    }
    /*int i;
    for(i = 1; i <= 50; i++)
        if(isPrime(i) == 1)
            printf("%d\n", i);*/
    //getch();
    
}

int isPrime(int n)
{
    int i;
    // See if the number is in the range < 4
    
    if(n <= 3)
    {
        // If the number is neither two nor three, then it is not prime otherwise it is prime
        if(n <= 1)
            return 0;
        else
            return 1;
    }
    else
    {
        // If the number is divisible by either two or three then it isn't prime
        if(n % 2 == 0 || n % 3 == 0)
            return 0;
        else
        {
            // If the number is of the form 6k+1 or 6k-1, then it is a Prime number unless it is divisible by another number of 
            // the form 6k-1 or 6k+1 , eg. 25
            for(i = 5; i <= (int)sqrt(n) + 1; i += 6)
                if(n % i == 0 || n % (i + 2) == 0)
                    return 0;
        }
    }
    return 1;
}
