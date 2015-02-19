#include <stdio.h>
void print_msg(char[]);
void skip(char*);
int y = 1;
int main()
{
    int x = 4;
    printf("Address of x: %p\n", &x);
    printf("Address of x: %d\n", &x);
    printf("Size: %d\n", sizeof(4));
    printf("Size: %d\n", sizeof("Saqib"));
    print_msg("My name is Saqib Nizam Shamsi");
    skip("Don't call me");

    return 0;
}
void print_msg(char msg[])
{
    printf("%s\n", msg);
    printf("Size: %d\n", sizeof(msg));
    printf("Address of msg: %p\n", msg);
}

void skip(char *msg)
{
    //puts((msg + 6));
    printf("%s\n", (msg + 6));
}
