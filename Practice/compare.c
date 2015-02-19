#include<stdio.h>
int main(int argc, char* argv[])
{
    int line, chr1, chr2, col, flag;
    FILE *expected, *generated;
    expected = fopen(argv[1], "r");
    generated = fopen(argv[2], "r");
    line = 1;
    col = 1;
    flag = 1;
    while((chr1 = getc(expected)) != EOF)
    {
        chr2 = getc(generated);
        if(chr1 == '\n')
            line++;
        if(chr1 != chr2)
        {
            printf("Mismatch at line: %d, column: %d\n", line, col);
            printf("Expected: %c\n", chr1);
            printf("Found: %c\n", chr2);
            flag = 0;
            break;
        }
    }
    if(flag == 1)
        printf("No Mismatches.");
    fclose(expected);
    fclose(generated);
    return 0;
}

