import java.util.ArrayList;
import java.util.List;

class Node {

	private int value;
	public Node next = null;

	Node(int val) {
		this.setValue(val);
	}

	public void setValue(int val) {
		this.value = val;
	}

	public int getValue() {
		return this.value;
	}
}

public class LinkedList {

	Node head;

	LinkedList() {
	}

	LinkedList(int[] srcArray) {
		for (int val : srcArray)
			this.addToBack(val);
	}

	public void addToFront(int val) {
		Node n = new Node(val);
		n.next = this.head;
		this.head = n;
	}

	public void addToBack(int val) {

		if (this.head == null) {
			this.head = new Node(val);
		} else {
			Node start = this.head;
			while (start.next != null) {
				start = start.next;
			}
			start.next = new Node(val);
		}
	}

	public Node remove(int index) {
		Node n = this.head;
		for (int i = 0; i < index - 1; i++) {
			n = n.next;
		}

		Node before = n;
		Node removed = n.next;
		Node after = removed.next;

		before.next = after;

		return removed;
	}

	public Node set(int index, Node node) {
		Node n = this.head;
		for (int i = 0; i < index - 1; i++) {
			n = n.next;
		}

		Node before = n;
		Node removed = n.next;
		Node after = removed.next;

		before.next = node;
		node.next = after;

		return removed;
	}

	public Node get(int index) {
		Node n = this.head;
		for (int i = 0; i < index; i++) {
			n = n.next;
		}
		return n;
	}

	public List<Node> toArrayList() {
		List<Node> l = new ArrayList<>();
		Node start = this.head;
		if (start == null) {
			return l;
		}
		for (;;) {
			l.add(start);
			if (start.next == null)
				break;
			start = start.next;
		}
		return l;
	}
}