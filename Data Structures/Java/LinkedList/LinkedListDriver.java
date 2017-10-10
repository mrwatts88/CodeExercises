import java.util.List;

public class LinkedListDriver {

	public static void main(String[] args) {
		LinkedList ll = new LinkedList();

		ll.addToBack(5);
		ll.addToBack(4);
		ll.addToBack(45);
		ll.addToBack(51);
		ll.addToBack(11);
		ll.addToBack(901);
		ll.addToBack(1);
		ll.addToBack(0);
		ll.addToFront(999);

		List<Node> list = ll.toArrayList();

		System.out.println("original list");

		for (Node n : list)
			System.out.println(n.getValue());

		System.out.println();

		Node switchedNode = ll.set(2, new Node(888));
		Node gotNode = ll.get(7);
		Node removedNode = ll.remove(6);

		System.out.println("switched out: " + switchedNode.getValue());
		System.out.println("got: " + gotNode.getValue());
		System.out.println("removed: " + removedNode.getValue());

		List<Node> manipulatedList = ll.toArrayList();

		for (Node n : manipulatedList)
			System.out.println(n.getValue());
	}
}