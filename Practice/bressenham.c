#include<stdio.h> 
#include<math.h> 
#include<conio.h> 
#include<graphics.h>

void bresen(int, int, int, int, int);

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
    
    bresen(x1,y1,x2,y2,c);  
    getch(); 
    closegraph(); 
    return 0;
}

void bresen(int x1,int y1,int x2,int y2, int c) 
{
     int Dx=x2-x1,Dy=y2-y1,i; 
     float xin,yin,X=x1,Y=y1,Derr,err=0.0; 
     
     Derr=abs(Dx/Dy);
     
     for(i=x1;i<=x2;i++)
     {
                        putpixel(i,Y,(c%16));
                        err+=Derr;
                        if(err>=0.5)
                        {
                                    Y+=1;
                                    err-=1.0;
                        }
     }
}
