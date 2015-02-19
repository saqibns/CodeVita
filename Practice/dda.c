#include<stdio.h> 
#include<math.h> 
#include<conio.h> 
#include<graphics.h>

void dda(int, int, int, int, int);

int main() 
{
    int x1,x2,y1,y2,c;
    int gd=DETECT,gm;

    printf("Enter the two values of co-ordiantes:\n"); 
    scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
    
    printf("\nEnter the color value:");
    scanf("%d",&c);
    initgraph(&gd,&gm,"");
    
    cleardevice();
    
    dda(x1,y1,x2,y2,c);  
    getch(); 
    closegraph(); 
    return 0;
}

void dda(int x1, int y1, int x2, int y2, int color)
{
    dx=abs(x2-x1);
    dy=abs(y2-y1);

    if(dx>=dy)
    pixel=dx;
    else
    pixel=dy;

    dx=dx/pixel;
    dy=dy/pixel;

    x=x1;
    y=y1;

    i=1;
    while(i<=pixel)
    {
          putpixel(x,y,color % 16);
          x=x+dx;
          y=y+dy;
          i=i+1;
    }
}
