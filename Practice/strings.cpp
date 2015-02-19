#include<iostream>
#include<string>
using namespace std;
int main()
{
    string stars(42, '*');
    cout << stars << endl;
    cout << string::npos << endl;

    string msg("My name is Saqib");
    cout << msg << endl;
    cout << msg[1] << endl;
    msg[0] = 'i';
    msg[1] = 's';
    msg.insert(0, "H");

    cout << msg << endl;
    string s;
    s = msg;
    s[1] = 'e';
    cout << msg.at(5) << endl;
    s[2] = msg.at(5);
    cout << s << endl;
    cout << msg << endl;
    return 0;
}
