#include<stdio.h> 
#include<math.h> 
#include<conio.h> 
#include<graphics.h>

void polynomial(int);

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
    
    polynomial(x1,y1,x2,y2,c);  
    getch(); 
    closegraph(); 
    return 0;
}

void polynomial(int r)
{
       float x=0;
       float y=0;
       float range=(r/sqrt(2));

       do
      {
         y=sqrt(pow(r,2)-pow(x,2));

         putpixel((int)(h+x+0.5),(int)(k+y+0.5),color);
         putpixel((int)(h+y+0.5),(int)(k+x+0.5),color);
         putpixel((int)(h+y+0.5),(int)(k-x+0.5),color);
         putpixel((int)(h+x+0.5),(int)(k-y+0.5),color);
         putpixel((int)(h-x+0.5),(int)(k-y+0.5),color);
         putpixel((int)(h-y+0.5),(int)(k-x+0.5),color);
         putpixel((int)(h-y+0.5),(int)(k+x+0.5),color);
         putpixel((int)(h-x+0.5),(int)(k+y+0.5),color);

         x+=0.05;
      }
       while(x<=range);
}
