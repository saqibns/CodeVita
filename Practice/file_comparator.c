#include<stdio.h>
int main(int argc, char* argv[])
{
    int line, chr1, chr2;
    FILE *expected, *generated;
    expected = fopen(argv[1], "r");
    generated = fopen(argv[2], "r");
    line = 1;
    while((chr1 = getc(expected)) != EOF)
    {
        chr2 = getc(generated);
        if(chr1 == '\n')
            line++;
        if(chr1 != chr2)
        {
            printf("Mismatch at: %d\n", line);
            break;
        }
    }
    fclose(expected);
    fclose(generated);
    return 0;
}

