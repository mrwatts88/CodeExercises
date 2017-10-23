// QuickSort
// Time Complexity: O(n log n)

#include "stdafx.h"
#include <iostream>

/// <params> array to be sorted, leftmost index, rightmost index
void quickSort(int arr[], int left, int right) { 

	int i = left;
	int j = right;
	int temp; // used for swapping
	int pivot = arr[(left + right) / 2]; // chosen to be middle element, but doesn't need to be.

	while (i <= j) {	// stop this partition when i and j switch sides

		while (arr[i] < pivot)	// find first element starting from each end that is on the wrong side of the pivot
			i++;	
		while (arr[j] > pivot)	
			j--;

		if (i <= j) {	// if i and j are still on correct sides, swap the 2 elements
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}		
	};


	if (j > left) {		// if there is still a subarray on the right, call quicksort on it
		quickSort(arr, left, j);
	}
	if (i < right) {	// if there is still a subarray on the 
		quickSort(arr, i, right);
	}
}

int main()
{
	int arr[] = { 1000, 7,8,5,7,6,44,99,-55,6,9,898, -45 };
	quickSort(arr, 0, sizeof(arr) / sizeof(*arr) - 1);
	for (int i = 0; i < sizeof(arr)/sizeof(*arr); i++) {
		std::cout << arr[i] << std::endl;
	}
	return 0;
}