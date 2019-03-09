package cuddly_journey;

public class BinarySearchTree<Q> {

	Node<Q> root = null;
	int no_of_nodes = 0;
	int height = 0;

	public BinarySearchTree() {
		root = new Node<Q>();
		no_of_nodes = 0;
		height = 0;
	}

	public boolean insert(Q val) {
		Node<Q> new_node = new Node<Q> (val);
		if (root==null)
		{
			root = new_node;
			return true;
		}
		return false;
	}

	public void find(Q val) {

	}

	public void delete(Q val) {

	}

	// Unit test purpose
	public static void main(String[] args) {

	}

	class Node<T> {
		T val;
		Node<T> left;
		Node<T> right;
		Node<T> parent;

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

}
