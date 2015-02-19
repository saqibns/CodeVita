#include<iostream>
#include<cstdio>
using namespace std;
int cycle_length(long long int);
int main()
{
    long long int from, to, maxx, tmp;
    while((scanf("%d %d", &from, &to)) != EOF)
    {
        maxx = cycle_length(from);
        if(from <= to)
        {
            for(long long int i = from + 1; i <= to; i++)
            {
                tmp = cycle_length(i);
                if(tmp > maxx)
                {
                    maxx = tmp;
                }
            }
        }
        else
        {
            for(long long int i = from + 1; i >= to; i--)
            {
                tmp = cycle_length(i);
                if(tmp > maxx)
                {
                    maxx = tmp;
                }
            }
        }

        printf("%d %d %d\n", from, to, maxx);
    }
        return 0;
}

int cycle_length(long long int num)
{
    int c = 0;
    while(num > 1)
    {
        if(num % 2 == 0)
            num /= 2;
        else
            num = 3 * num + 1;
        c++;
    }
    return (c + 1);
}

