#define NO_OF_DIGITS 9
#include<iostream>
#include<cmath>

using namespace std;

void add_arrays();
void display();

int num_one[NO_OF_DIGITS];
int num_two[NO_OF_DIGITS];
int sum[NO_OF_DIGITS];

int main()
{
    /*Get the number of students*/
    int i, n, before_decimal, after;
    float total = 0, per_student, after_decimal, net = 0.0, tmp, amount[100];
    cin >> n;
    /*Get the amount spent by each student*/
    for(i = 0; i < n; i++)
    {
        cin >> amount[i];
        total += amount[i];
    }

    per_student = total / n;
    /*before_decimal = floor(per_student);
    after_decimal = per_student - before_decimal;
    after = (int) 100 * after_decimal;
    per_student = before_decimal + after / 100;

    cout << "Per Student:" <<per_student << endl;
    */

    for(i = 0; i < n; i++)
    {
        tmp = amount[i] - per_student;
        before_decimal = floor(tmp);
        after_decimal = tmp - before_decimal;
        after = (int) 100 * after_decimal;
        tmp = before_decimal + after / 100;
        if(tmp > 0)
            net += tmp;
    }
    printf("%.2f", net);
    return 0;


}

void add_arrays()
{
    int i, tmp, carry = 0;
    for(i = NO_OF_DIGITS - 1; i > 0; i--)
    {
        tmp = num_one[i] + num_two[i] + carry;
        sum[i] = tmp % 10;
        carry = tmp / 10;
    }
    sum[0] = carry;
}

void display(int a[NO_OF_DIGITS])
{
    int i;
    for(i = 0; i < NO_OF_DIGITS - 3; i++)
    {
        if(a[i] != 0)
            cout << a[i];
    }
    cout << ".";
    cout << a[NO_OF_DIGITS - 2];
    cout << a[NO_OF_DIGITS - 1];
    cout << endl;
}

