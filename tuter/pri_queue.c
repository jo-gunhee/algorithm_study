#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
int heap[MAX_SIZE];

void push(int item, int *n)
{
	int i = 0;
	i = ++(*n);

/* 개념은 부모-자식 간 비교하면서 즉시 서로 자리를 바꾸는 것이지만 */
/* 실제 코드 구현상에서는 들어올 자식보다 작았던 부모는 먼저 그 자리로 바꾼 뒤 */
/* while문 빠져나올 때 새로 들어올 자식을 최종적으로 넣으면 됨. */

	while ((i != 1) && item < heap[i/2]) {
		heap[i] = heap[i / 2]; // 원래 자식 들어갈 자리에 부모의 값 저장
		i = i / 2; // 새로 들어올 자식이 기존 부모자리에 들어갈 것을 대비해 i를 반 줄임
	}
	heap[i] = item;
}

int main(void)
{
	int input;
	int n = 0, count = 0;

	printf("Min Heap 구현 - 숫자를 입력하세요.\n");
	printf("*****숫자 입력(-1을 입력하면 입력 종료)*****\n");

	while (1)
	{
		scanf("%d", &input);

		if (input == -1)
			break;

		push(input, &n);
		count++;
	}

   printf("Level Order Traversal : ");
	for (int i = 1; i <= count; i++) {
		printf("%d ", heap[i]);
	}

}