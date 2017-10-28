public class BSTNode {
	private BSTNode left;
	private BSTNode right;
	public int value;

	public BSTNode(int val) {
		value = val;
	}

	public void add(BSTNode n) {
		if (n.value <= value)
			addLeft(n);
		else
			addRight(n);
	}

	public void addLeft(BSTNode n) {
		if (left == null)
			left = n;
		else
			left.add(n);
	}

	public void addRight(BSTNode n) {
		if (right == null)
			right = n;
		else
			right.add(n);
	}

	public void toStringg() {
		if (this.left != null)
			this.left.toStringg();
		System.out.print(this.value + " ");
		if (this.right != null)
			this.right.toStringg();
	}
}