#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int i, students[100], n, total = 0, ps, tmp, net = 0;
    float amt, per_student;
    cin >> n;
    while (n != 0)
    {
        total = 0;
        net = 0;
        for(i = 0; i < n; i++)
        {
            cin >> amt;
            students[i] = amt * 1000;
            total += students[i];
        }
        per_student = total / n;
        ps = (int) per_student;
        for(i = 0; i < n; i++)
        {
            tmp = students[i] - ps;
            tmp = tmp / 10;
            if(tmp > 0)
                net += tmp;
        }
        //printf("%d\n", net);
        printf("%.2f\n", (float) net / 100);
        cin >> n;
    }
    return 0;
}


