import java.util.Arrays;

public class BubbleSort {

	public static void main(String[] args) {
		int[] arr = new int[20];

		for (int i = 0; i < arr.length; i++)
			arr[i] = (int) (Math.random() * 100);

		bubbleSort(arr);
		for (int x : arr) {
			System.out.print(x + " ");
		}
		System.out.println();

		int[] arr2 = Arrays.copyOf(arr, arr.length);

		bubbleSortRecursive(arr2, arr2.length);
		for (int x : arr2) {
			System.out.print(x + " ");
		}
	}

	public static void bubbleSort(int[] arr) {
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = 0; j < arr.length - i - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					int temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
	}

	public static void bubbleSortRecursive(int[] arr, int arrayLength) {
		if (arrayLength == 1)
			return;

		for (int j = 0; j < arrayLength - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
		bubbleSortRecursive(arr, arrayLength - 1);
	}
}

// Time Complexity
// Omega(n)
// Theta(n^2)
// O(n^2)

// Space Complexity
// O(1)