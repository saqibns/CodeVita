#include<iostream>
#include<string>
using namespace std;
int main()
{
    string x, y;
    cin >> x >> y;
    int sum = 0;
    int alpha[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for(int i = 0 ; i < x.length() ; i++)
        alpha[x[i] - 'a'] += 1;
    for(int j = 0 ; j < y.length() ; j++)
        alpha[y[j] - 'a'] -= 1;
    for(int k = 0 ; k < 26 ; k++)
        sum += abs(alpha[k]);

    cout << sum << endl;
    return 0;
}
