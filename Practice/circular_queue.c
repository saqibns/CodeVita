#define LEN 3
#include<stdio.h>
void enqueue(int);
int dequeue();
void status();

int q[LEN], front, rear;
int main()
{
    front = rear = -1;
    int choice, item;
    while(1)
    {
        scanf("%d", &choice);
        switch(choice)
        {
        case 1:
            scanf("%d", &item);
            enqueue(item);
            break;
        case 2:
            printf("%d\n", dequeue());
            break;
        case 3:
            status();
            break;
        default:
            printf("Invalid Choice\n");
            break;
        }
    }
    return 0;
}

void enqueue(int item)
{
    if(front == -1)
    {
        front = 1;
        rear = 0;
        q[0] = item;
    }

    else if(front == rear)
    {
        printf("Queue is Full\n");
    }
    else
    {
        q[front] = item;
        front = (front + 1) % LEN;
    }
}

int dequeue()
{
    int item;
    if(front == -1 && rear == -1)
    {
        printf("Queue is Empty\n");
        return -1;
    }
    else
    {
        item = q[rear];
        q[rear] = 0;
        rear = (rear + 1) % LEN;
        if(rear == front)
            rear = front = -1;
        return item;
    }
}

void status()
{
    int i;
    for(i = 0; i < LEN; i++)
        printf("%d ", q[i]);
    printf("\n");
}

