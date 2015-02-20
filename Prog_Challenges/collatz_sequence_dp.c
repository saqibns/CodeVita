#define SIZE 1000000
#include<stdio.h>
long long steps[SIZE];
long long sequence(long long);
void display(long long[], long long);
int main()
{
    long long i, from, to, start, end, max, tmp;
    for(i = 0; i < SIZE; i++)
    {
        steps[i] = 0;
    }
    steps[1] = 1;
    steps[2] = 2;
    while(scanf("%lld %lld", &from, &to) != EOF)
    {
        max = 0;
        if(from < to)
        {
            start = from;
            end = to;
        }
        else
        {
            start = to;
            end = from;
        }
        for(i = start; i <= end; i++)
        {
            tmp = sequence(i);
            if(tmp > max)
                max = tmp;

        }
        printf("%lld %lld %lld\n", from, to, max);

    }
    return 0;
}

long long sequence(long long n)
{
    if(n < SIZE && steps[n] != 0)
    {
        return steps[n];
    }
    else
    {
        if(n % 2 == 0)
        {
            if(n < SIZE)
            {
                steps[n] = 1 + sequence(n / 2);
                return steps[n];
            }
            else
                return 1 + sequence(n / 2);
        }
        else
        {
            if(n < SIZE)
            {
                steps[n] = 1 + sequence(3 * n + 1);
                return steps[n];
            }
            else
                return 1 + sequence(3 * n + 1);
        }
    }


}


