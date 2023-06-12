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
	listint_t *cur = NULL;

	if (*head == NULL)
	{
		printf("hello");
		return (1);
	}

	cur = *head;

	while (cur->next != NULL)
	{
		printf("%d", cur->n);
		cur = cur->next;
	}
	return (1);
}
