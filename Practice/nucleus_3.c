#include<stdio.h>
int main()
{
int n,j;
for(n=1;n<=10;n++)
{
j=1;
sos:
if(j<=n)
{
printf("%2d ",n*j);
j++;
goto sos;
}
else
{
printf("\n");

continue;
}

}

return 0;
}
