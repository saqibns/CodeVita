#include<stdio.h>
#include<math.h>

int find_trailing_zeroes(int);
int exponent(int, int);

int main()
{
    int i, test_cases, number;
    // Get the number of test cases
    
    scanf("%d", &test_cases);
    //printf("%d", test_cases);
    
    // For each test case, get a number and calculate its trailing zeroes
    
    for(i = 1; i <= test_cases; i++)
    {
        scanf("%d", &number);
        //printf("%d", number);
        printf("%d\n", find_trailing_zeroes(number));
    }
    
//    printf("%d\n", exponent(5, 2));
//    printf("%d\n", exponent(5, 3));
//    printf("%d\n", exponent(2, 5));
    
    //getch();
    
    
//    printf("%d\n", find_trailing_zeroes(3));
//    printf("%d\n", find_trailing_zeroes(60));
//    printf("%d\n", find_trailing_zeroes(100));
//    printf("%d\n", find_trailing_zeroes(1024));
//    printf("%d\n", find_trailing_zeroes(23456));
//    printf("%d\n", find_trailing_zeroes(8735373));

    
    //getch();
    return 0;
}

int find_trailing_zeroes(int n)
{
    // Run a loop until a power of five gives a number less than zero
    
    int factors, zeroes, index, power;
    zeroes = 0;
    power = 5;
    index = 2;
    while((factors = (n / power)) > 0)
    {
        zeroes += factors;
        //printf("%f %d\n", power, factors);
        power = exponent(5, index);
        index++;
    }
    
    return zeroes;
}

int exponent(base, index)
{
    int i, expnt = 1;
    for(i = 1; i <= index; i++)
        expnt *= base;
    return expnt;
}
