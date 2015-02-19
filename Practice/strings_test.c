#include<stdio.h>
#include<string.h>
int my_len(const char*);
int main()
{
    const char* one = "Saqib";
    const char* sub = "qib";
    printf("%d\n", strstr(one, sub) - one);
    printf("%d\n", sizeof(one));
    printf("%d\n", strlen(one));
    printf("%d\n", my_len(one));

    one = "Shamsi";
    printf("%d\n", my_len(one));
    return 0;
}

int my_len(const char* str)
{
    int i = 0;
    while(*(str + i) != '\0')
        i++;
    return i;
}
