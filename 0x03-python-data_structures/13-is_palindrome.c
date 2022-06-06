#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: True if it is a palindrome, False if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current;
	listint_t *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = malloc(sizeof(listint_t));
	if (current != NULL)
		current = *head;
	while (current != NULL)
	{
		current = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	current = prev;

	while ((*head)->next != NULL && current->next != NULL)
	{
		if ((*head)->n != current->n)
		{
			return (0);
		}
	}

	return (1);
}
