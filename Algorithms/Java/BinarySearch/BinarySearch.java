public class BinarySearch {

	private static int leftIndex = 0;
	private static int rightIndex = 0;
	private static int searchIndex = 0;

	public static int search(int[] arr, int el) {

		rightIndex = arr.length - 1;
		searchIndex = rightIndex / 2;
		System.out.println("left: " + leftIndex + "\nright: " + rightIndex + "\nsearch: " + searchIndex);
		while (leftIndex <= rightIndex) {
			if (arr[searchIndex] == el) {
				return searchIndex;
			} else if (arr[searchIndex] < el) {
				leftIndex = searchIndex + 1;
				searchIndex = (leftIndex + rightIndex) / 2;
				System.out.println("left: " + leftIndex + "\nright: " + rightIndex + "\nsearch: " + searchIndex);

			} else if (arr[searchIndex] > el) {
				rightIndex = searchIndex - 1;
				searchIndex = (leftIndex + rightIndex) / 2;
				System.out.println("left: " + leftIndex + "\nright: " + rightIndex + "\nsearch: " + searchIndex);

			}
		}
		return -1;
	}
}
