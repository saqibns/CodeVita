#include<stdio.h>
void neighbours(int[][], int, int);
int chk(int, int, int);
int main()
{
    int i, j, ii, jj, count, r;
    count = 1;
    /*int a[8][2];
    neighbours(a, 1, 1);
    for(i = 0; i < 8; i++)
        printf("(%d, %d)\n", a[i][0], a[i][1]);
        */
    /*printf("%d\n", chk(1, 2, 3));
    printf("%d\n", chk(4, 1, 7));
    printf("%d\n", chk(-1, 0, 8));
    printf("%d\n", chk(9, 0, 8));
    */
    scanf("%d %d", &i, &j);
    while(i != 0 && j != 0)
    {
        int a[i][j], nbrs[i][j];
        for(ii = 0; ii < i; ii++)
            for(jj = 0; jj < j; jj++)
                a[ii][jj] = 0;

        char lines[i + 1][j + 1];
        for(ii = 0; ii < i; ii++)
        {
            scanf("%s", lines[ii]);
            /*printf("%s\n", lines[ii]);*/
        }
        for(ii = 0; ii < i; ii++)
            for(jj = 0; jj < j; jj++)
        {
            if(lines[ii][jj] == '*')
            {
                neighbours(nbrs, ii, jj);
                for(r = 0; r < 8; r++)
                {
                    if(chk(nbrs[r][0], 0, i - 1) == 1 && chk(nbrs[r][1], 0, j - 1) == 1)
                        a[nbrs[r][0]][nbrs[r][1]] += 1;
                }
            }
        }

        printf("Field #%d:\n", count);
        for(ii = 0; ii < i; ii++)
        {
            for(jj = 0; jj < j; jj++)
            {
                if(lines[ii][jj] == '*')
                    printf("*");
                else
                    printf("%d", a[ii][jj]);
            }
            printf("\n");
        }
        /* Mine Status goes here */
        scanf("%d %d", &i, &j);
        count++;
    }
    return 0;
}

void neighbours(int a[8][2], int x, int y)
{
    /*printf("%d %d\n", x, y);*/
    a[0][0] = x - 1; a[0][1] = y - 1;
    a[1][0] = x - 1; a[1][1] = y;
    a[2][0] = x - 1; a[2][1] = y + 1;
    a[3][0] = x; a[3][1] = y - 1;
    a[4][0] = x; a[4][1] = y + 1;
    a[5][0] = x + 1; a[5][1] = y - 1;
    a[6][0] = x + 1; a[6][1] = y;
    a[7][0] = x + 1; a[7][1] = y + 1;
}

int chk(int x, int lower, int upper)
{
    if(x >= lower && x <= upper)
        return 1;
    return 0;
}
