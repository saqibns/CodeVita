#include<iostream>
#include<sstream>
using namespace std;
int cycle_length(long long int);
int main()
{
    string line;
    long long int from, to, maxx, tmp;
    getline(cin, line);
    while(line != "" && line != "\n")
    //while(line != string(EOF))
    {
        stringstream linestream(line);
        linestream >> from >> to;
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

        cout << from << " " << to << " " << maxx << endl;
        getline(cin, line);
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
