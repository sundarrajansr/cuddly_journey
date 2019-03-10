package cuddly_journey;

public class BinarySearchTree<Q extends Comparable<Q>> {

	Node<Q> root = null;
	int no_of_nodes = 0;
	int height = 0;

	public BinarySearchTree() {
		root = null;
		no_of_nodes = 0;
		height = 0;
	}

	public boolean insert(Q val) {
		Node<Q> new_node = new Node<Q>(val);
		if (root == null) {
			root = new_node;
			return true;
		}

		Node<Q> cnode = root;
		Node<Q> parent = null;
		while (true) {
			parent = cnode;
			int compare = val.compareTo(cnode.val());
			if (compare <= 0) {
				cnode = cnode.left();
				if (cnode == null) {
					parent.setLeft(new_node);
					return true;
				}
			} else if (compare > 0) {
				cnode = cnode.right();
				if (cnode == null) {
					parent.setRight(new_node);
					return true;
				}
			}
		}
	}

	public void print() {
		if (root != null)
			printAllNodes(root);
		else
			System.out.println("Warning - Empty Tree");
	}

	private void printAllNodes(Node<Q> node) {
		System.out.printf("Node : %s, Left : %s, Right : %s\n", node.val(),
				node.left() == null ? "null" : node.left().val(), node.right() == null ? "null" : node.right().val());
		if (node.left() != null)
			printAllNodes(node.left());
		if (node.right() != null)
			printAllNodes(node.right());

	}

	public void find(Q val) {

	}

	public void delete(Q val) {

	}

	class Node<T> {
		T val;
		private Node<T> left;
		private Node<T> right;
		private Node<T> parent;

		public Node() {
			val = null;
			left = null;
			right = null;
			parent = null;
		}

		public Node(T val) {
			this();
			this.val = val;
		}

		public void setLeft(Node<T> obj) {
			this.left = obj;
		}

		public void setRight(Node<T> obj) {
			this.right = obj;
		}

		public void setParent(Node<T> obj) {
			this.parent = obj;
		}

		public Node<T> left() {
			return this.left;
		}

		public Node<T> right() {
			return this.right;
		}

		public Node<T> parent() {
			return this.parent;
		}

		public void setVal(T newobj) {
			this.val = newobj;
		}

		public T val() {
			return val;
		}
	}

	// Unit test purpose
	public static void main(String[] args) {
		BinarySearchTree<Integer> bst = new BinarySearchTree<Integer>();
		bst.insert(5);
		bst.insert(25);
		bst.insert(15);
		bst.insert(10);
		bst.insert(35);
		bst.print();
	}

}
