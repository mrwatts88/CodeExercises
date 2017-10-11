#include "stdafx.h"
#include <iostream>
#include <vector>
#include "LinkedList.h"

using namespace std;

int main()
{
	LinkedList ll(vector<int>{ 4, 4, 8, 6, 8, 0 });
	ll.addToBeginning(99);
	return 0;
}