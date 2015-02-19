#include<stdio.h>
int main()
{
int t=1,i=1,j=1,n;
scanf("%d",&n);
while(t<=n)
{
printf("%2d ",i*t);
if(i==j)
{
j++;
i=1;
t++;
printf("\n");
continue;
}
else
{
i++;
}

}
return 0;
}

