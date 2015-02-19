#include<iostream>

namespace first
{
    int power = 3;
    namespace second
    {
        int energy = 1;
    }
}

int main()
{
    std::cout << first::power << std::endl;
    std::cout << first::second::energy << std::endl;
    return 0;
}
