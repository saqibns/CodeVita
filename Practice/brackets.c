#define BUFFER_SIZE 10
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int line[BUFFER_SIZE], number, i, count = 1;
    number = fread(line, 1, BUFFER_SIZE, stdin);
    while(count < 1)
    {
        for(i = 0; i < number; i++)
        if(line[i] == '\n')
        {
            printf("%c\n", line[i]);
            brea
        
    
    getch();
    return 0;
}
