#include "stdafx.h"
#include "LinkedList.h"
LinkedList::LinkedList()
{
}

LinkedList::LinkedList(vector<int> vec)
{
	for (int x : vec)	// size of array is not known, and would need to be passed in to use range-based for loop, so use a vector
		addToEnd(x);
}

LinkedList::~LinkedList()
{
}

void LinkedList::addToBeginning(int value) {

	Node *n = new Node;
	n->value = value;
	n->next = head;
	head = n;
}

void LinkedList::addToEnd(int value) {
	Node *n = new Node;
	n->value = value;

	Node *ref = this->head; // "this->" is optional

	if (ref == NULL) {
		this->head = n;
	}
	else {

		while (ref->next != NULL)
		{
			ref = ref->next;
		}

		ref->next = n;
	}
}