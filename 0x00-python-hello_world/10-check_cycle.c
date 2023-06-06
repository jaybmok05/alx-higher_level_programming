#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked
 * list has a cycle in it.
 * @list: the list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tort_ptr = list;
	listint_t *hare_ptr = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	/* Iterate through the list using the hare and tortoise pointers */
	for (; hare_ptr && hare_ptr->next; tort_ptr = tort_ptr->next,
			hare_ptr = hare_ptr->next->next)
	{
		/*hare and tortoise pointers meet, a cycle is detected */
		if (tort_ptr == hare_ptr)
		{
			return (1);
		}
	}

	return (0);
}

