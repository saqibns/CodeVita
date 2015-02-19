#include<iostream>
#include<sstream>
using namespace std;

long long int cycle_length(long long int);
int main()
{
    string line;
    long long int from, to;
    getline(cin, line);
    while(line != "" && line != "\n")
    {
        stringstream linestream(line);
        linestream >> from >> to;
        long long int a[to - from + 1];
        long long int largest[to - from + 1];
        long long int idx = 0;
        for(long long int i = from; i <= to; i++)
        {
            a[idx] = cycle_length(i);
            largest[idx] = i;
            idx++;
        }
        long long int m = a[0];
        long long int z = largest[0];
        for(long long int i = 1; i < to - from + 1; i++)
        {
            if(a[i] > m)
            {
                m = a[i];
                z = largest[i];
            }
        }
        cout << from << " " << to << " " << m << endl;
        //cout << "Largest:" << z << endl;
    getline(cin, line);
    }
    return 0;
}

long long int cycle_length(long long int num)
{
    long long c = 0;
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

