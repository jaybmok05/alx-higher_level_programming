#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into
 * a sorted singly linked list.
 * @head: pointer to the first node
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;


	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}


	runner = *head;

	while (runner->next != NULL && runner->next->n < number)
	{
		runner = runner->next;
	}

	new_node->next = runner->next;
	runner->next = new_node;

	return (new_node);
}
