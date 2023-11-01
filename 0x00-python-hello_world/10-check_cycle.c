#include "lists.h"
/**
 * check_cycle - function checks if it a cycle linked list
 * @list: the linked list
 * Return: 0 if no cycle and 1 if there is cycle
*/
int check_cycle(listint_t *list)
{
listint_t *fast = NULL;
listint_t *slow = NULL;

if (!list)
{
return (0);
}
fast = list;
slow = list;
while (fast && slow && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (fast == slow)
{
return (1);
}
}
return (0);
}
