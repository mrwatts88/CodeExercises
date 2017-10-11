#pragma once
#include <vector>

using namespace std;

struct Node {
	int value;
	Node *next = NULL;  // next must be a pointer; a class or struct cannot have a member of the same type of itself.
};

class LinkedList
{
private:
	Node *head = NULL; //declare access modifiers with : then list all members, instead of individually.

public:
	LinkedList();
	LinkedList(vector<int> vec);
	~LinkedList();
	void addToBeginning(int value);
	void addToEnd(int value);
};

