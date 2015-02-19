#include<iostream>
using namespace std;

class Person
{
    private:
        string name;
        int age;
        const int id;

    public:
        Person()
        : id(900)
        {
            name = "John Doe";
            age = 0;
        }

        Person(string n, int a, int i)
        : id(i)
        {
            name = n;
            age = a;
        }

        void next_year()
        {
            cout << "Hello, " << name << ". Next year you will be " << age + 1 << " years old." << endl;
        }
};

int main()
{
    Person* p;
    Person q("Naruto", 16, 9009);
    p = &q;
    p -> next_year();
    return 0;
}
