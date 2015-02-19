#include <iostream>
#include <cstdlib>

int main()
{
    int i;
    for(i = 1 ; i <= 25 ; i++)
    {
        std::cout << rand() % 6 + 1 << std::endl;
    }
    return 0;
}
