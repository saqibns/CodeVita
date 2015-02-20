#include<iostream>

using namespace std;
int main()
{
    int tests;
    int m, n, c, flag;
    cin >> tests;
    while(tests--)
    {
        c = 0;
        cin >> n >> m;
        int a[m];
        for(int i = 0 ; i < m ; i++)
        {
            cin >> a[i];
        }

        for(int i = 1 ; i <= n ; i++)
        {
            flag = 1;
            for(int j = 0; j < m ; j++)
            {
                if(i % a[j] != 0)
                    {
                        flag = 0;
                        break;
                    }
            }
            if(flag == 1)
                c++;
        }
        cout << c << endl;

    }
    return 0;
}
