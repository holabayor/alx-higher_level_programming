#include "lists.h"

/**
 * insert_node - inserts a value on a position
 * @head: pointer to head of list
 * @number: the number to be inserted
 * Return: number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
			break;
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
