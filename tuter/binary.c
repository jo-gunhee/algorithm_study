#include <stdio.h>
#include <stdlib.h>
typedef struct _node{
int data;
struct _node * rightChild;
struct _node * leftChild;
}Node;

typedef Node * treePointer;

treePointer Create() { // 신규 노드 생성 함수
    treePointer node = (treePointer)malloc(sizeof(*node));
    node->rightChild = NULL;
    node->leftChild = NULL; // 신규노드 생성 시 일단 left/right NULL로 초기화
    return node;
}

void Inorder(treePointer ptr) { // 중위순회 함수. 재귀적으로 구현했음에 유의한다.
    if (ptr) // ptr이 NULL이 아닐 때만 if문을 돈다.
    {
        Inorder(ptr->leftChild);
        printf("%c ", ptr->data);
        Inorder(ptr->rightChild); // 왼쪽 - 중간 - 오른쪽 순으로 생각하면 편함
    }
}

int main(void)
{
    treePointer root = Create();
    treePointer N1 = Create();
    treePointer N2 = Create();
    root->data = 'A'; N1->data = 'B'; N2->data = 'C'; // 값 저장
    root->leftChild = N1; root->rightChild = N2; // root 노드에 N1, N2 연결
    Inorder(root);
}
