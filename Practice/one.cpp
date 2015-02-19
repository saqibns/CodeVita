#include <iostream>

class Message
{
public:
    void hello()
    {
        std :: cout << "Hello, World!" << std :: endl;
    }

    void customMessage(char* msg)
    {
        std :: cout << msg << std :: endl;
    }
};
int main()
{
    Message msg;
    std :: cout << "Did it!" << std :: endl;
    msg.hello();
    msg.customMessage("Saqib Nizam Shamsi");
}
