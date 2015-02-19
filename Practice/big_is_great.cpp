#include <iostream>
#include <string>

int main()
{
    std::string str;
    int tests;
    std::cin >> tests;
    while(tests--)
    {
        std::cin >> str;
        if(std::next_permutation(str.begin(), str.end()))
           std::cout << str << std::endl;
        else
            std:: cout << "no answer" << std::endl;
    }
    return 0;

}
