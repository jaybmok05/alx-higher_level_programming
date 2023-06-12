#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - a function in C that checks if a singly
 * linked list is a palindrome.
 * @head: pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;
	listint_t *temp;

	/*Find the middle of the linked list*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	
	/* move the slow pointer one step ahead, if odd nums*/
	if (fast != NULL)
	{
		slow = slow->next;
	}

	/*Compare first and second half of the linked list*/
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return 0;
		}
		prev = prev->next;
		slow = slow->next;
	}
	
	return 1;
}
