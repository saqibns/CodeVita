#include<stdio.h>
int main()
{
    typedef union
    {
        int count;
        float weight;
        float volume;
    }
    quantity;

    typedef struct
    {
        const char* name;
        const char* country;
        quantity amount;
    }
    order;

    order apples = {"Apples", "Cuba", .amount.weight = 1000.0};
    printf("%s %s %f", apples.name, apples.country, apples.amount.weight);
    return 0;
}
