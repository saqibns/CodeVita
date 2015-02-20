#include<iostream>
using namespace std;
int largest(int[], int);
int lcm(int[], int, int, int);
int main()
{
    int m, p, c, n, z;
    int tests;
    cin >> tests;
    while(tests--)
    {
        cin >> n >> z;
        int a[z];
        for(int k = 0; k < z; k++)
            cin >> a[k];
        m = a[0]; p = 1; c = 0;
        for(int i = 0 ; i < z ; i++)
        {
            p *= a[i];
            if(a[i] > m)
                m = a[i];
        }

        int l, f;
        l = lcm(a, z, p, m);
        f = l;
        while(l <= n)
        {
            c++;
            l += f;
        }
        cout << c << endl;
    }
    return 0;
}

int lcm(int a[], int len, int product, int large)
{
    int flag;
    for(int i = large; i <= product; i++)
    {
        flag = 1;
            for(int j = 0; j < len ; j++)
            {
                if(i % a[j] != 0)
                    {
                        flag = 0;
                        break;
                    }
            }
            if(flag == 1)
                return i;
    }
    return product;
}

