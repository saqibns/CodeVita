#include <iostream>
using namespace std;
int main()
{
    int length, i, j, key;
    cin >> length;
    int a[length];
    for(i = 0 ; i < length ; i++)
        cin >> a[i];

//    for(i = 0 ; i < length ; i++)
//        cout << a[i] << " ";
//    cout << endl;
    key = a[0];

    for(j = 1 ; j < length ; j++)
    {
        //cout << j << " ";
        key = a[j];
        i = j - 1;
        while(i >= 0 && a[i] > key)
        {
            a[i + 1] = a[i];
            i--;
        }
        a[i + 1] = key;
        for(i = 0 ; i < length ; i++)
            cout << a[i] << " ";
        cout << endl;
    }



}

