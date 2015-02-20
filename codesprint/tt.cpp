#include<iostream>
using namespace std;
int lcm(int[], int, int, int);
int main()
{
    int l;
    int a[] = {2, 3};
    l = lcm(a, 2, 6, 3);
    cout << l << endl;
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
