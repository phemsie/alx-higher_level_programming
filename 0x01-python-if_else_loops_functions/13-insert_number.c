#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - function in C that inserts a number into a sorted 
 * singly linked list
 * @head: a double pointer to the first node of the list
 * @number: the number to insert
 * Return: returns the address of the new node (ON SUCCESS) 
 * returns NULL (ON FAILURE)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!(*head))
		*head = new;
	else if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->n <= number && current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;

				return (new);
			}
			current = current->next;
		}
		if (current->next == NULL && current->n <= number)
			current->next = new;
	}
	return (new);
}
