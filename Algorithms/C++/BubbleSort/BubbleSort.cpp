// BubbleSort.cpp
// Time Complexity = O(n^2)

#include "stdafx.h"
#include <iostream>

using namespace std;

void bubbleSort(int arr[], int n) {
	bool swapped = true;
	int j = 0;
	int temp;

	while (swapped) {	// If an entire pass is made without a swap, the array is sorted and the sort can stop
		swapped = false;
		j++;
		for (int i = 0; i < n - j; i++) {
			if (arr[i] > arr[i + 1]) {
				temp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = temp;
				swapped = true;
			}
		}
	}
}

int main()
{
	int arr[] = { 4,9,4,-9,557,-233,0,88,6 };
	for (int i = 0; i < sizeof(arr) / sizeof(*arr); i++) {
		cout << arr[i] << " ";
	}
	cout << endl;

	bubbleSort(arr, sizeof(arr) / sizeof(*arr));

	for (int i = 0; i < sizeof(arr) / sizeof(*arr); i++) {
		cout << arr[i] << " ";
	}
	cout << endl;

    return 0;
}

