#include <iostream>
#include <string>

class Names
{
    public:
        void setName(std::string n)
        {
            name = n;
        }

        std::string getName()
        {
            return name;
        }

    private:
        std::string name;
};

int main()
{
    Names names;
    std::cout << names.getName() << std::endl;
    names.setName("Saqib Nizam Shamsi");
    std::cout << names.getName() << std::endl;
    return 0;
}
