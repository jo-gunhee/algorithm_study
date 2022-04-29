#include <stdio.h>
#define MAX 100
int front=-1;
int rear=-1;
int queue[MAX];
 
int isEmpty(void){
    if(front==rear) return 1;
    else return 0;
}
int isFull(void){
    int tmp=(rear+1)%MAX;
    if(tmp==front) return 1;
    else return 0;
}
void push(int value){
    if(isFull())
        printf("Queue is Full.\n");
    else{
    rear = (rear+1)%MAX;
    queue[rear]=value;
    }
}

int pop(){
    if(isEmpty()){
        printf("Queue is Empty.\n");
        return 0;
    }
    else{
        front = (front+1)%MAX;
        return queue[front];
    }
}
 
int main(){
    
    push(4);
    push(7);
    push(12);
    printf("%d\n",pop());
    printf("%d\n",pop());
    printf("%d\n",pop());
    pop();
    
    return 0;
}
