#include <stdio.h>
#include <stdlib.h>

/*check_cycle - To check if a singly linked list has a cycle
 *
 * Return: 0 if there is no cycle, 1 if cycle is detected
 */
int check_cycle(listint_t *list);
{
	struct listnode {
		int val;
		struct listnode* next;
	};
	int gotcycle(struct listnode* head){
		struct listnode* slow = head;
		struct listnode* fast = head;
	};
	while (fast != NULL && fast->next != NULL){
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast){
			return 1;
		}
	}
	return 0;
}
