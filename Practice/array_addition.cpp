#include<iostream>
int num_one[4] = {0, 1, 3, 5};
int num_two[4] = {0, 8, 8, 9};
int sum[4];
void add_arrays();
int main()
{
    int i;
    for(i = 0; i < 4; i++)
        std::cout << num_one[i];
    std::cout << std::endl;
    for(i = 0; i < 4; i++)
        std::cout << num_two[i];
    std::cout << std::endl;
    add_arrays();
    for(i = 0; i < 4; i++)
        std::cout << sum[i];
    std::cout << std::endl;
    return 0;
}

void add_arrays()
{
    int i, tmp, carry = 0;
    for(i = NO_OF_DIGITS - 1; i > 0; i--)
    {
        tmp = num_one[i] + num_two[i] + carry;
        sum[i] = tmp % 10;
        carry = tmp / 10;
    }
    sum[0] = carry;
}
