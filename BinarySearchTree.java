package cuddly_journey;
/*
 * todo
 * 
 * find the height
 * find the vertical traversal
 * print the tree in tree structure level by level
 * find successor , predecessor
 * support deletion
 * validate bst
 * order traversal with callback
 * support balancing with AVL
 * support balancing with red-black
 * treap
 * 
 */


public class BinarySearchTree<Q extends Comparable<Q>> {

	Node<Q> root = null;
	int no_of_nodes = 0;
	int height = 0;

	public BinarySearchTree() {
		root = null;
		no_of_nodes = 0;
		height = 0;
	}

	public BinarySearchTree<Q> insert(Q val) {

		Node<Q> new_node = new Node<Q>(val);

		// if Tree is Empty
		if (root == null) {
			root = new_node;
			return this;
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
					return this;
				}
			} else if (compare > 0) {
				cnode = cnode.right();
				if (cnode == null) {
					parent.setRight(new_node);
					return this;
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

	public Q find(Q val) {
		
		Node<Q> pointer = root;
		while (pointer!=null)
		{
			int diff = pointer.val().compareTo(val);
			if(diff==0) {
				return pointer.val();
			}else if (diff <0)
			{
				pointer = pointer.right();
			}
			else
			{
				pointer =pointer.left();
			}
		}
		return null;

	}

	public int width() {
		int left_width = 0;
		int right_width = 0;
		if (root == null)
			return 0;
		Node<Q> cnode = root;
		while (cnode.left() != null) {
			cnode = cnode.left();
			left_width++;
		}
		cnode = root;
		while (cnode.right() != null) {
			cnode = cnode.right();
			right_width++;
		}
		return left_width + right_width;

	}

	public int height() {

		return height;

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
		bst.insert(5).insert(3).insert(2).insert(1).insert(4).insert(10).insert(15).insert(12);
		bst.print();
		System.out.println(bst.find(3));
		System.out.println(bst.find(22));
		System.out.println(bst.find(12));
		System.out.println("width" + bst.width());
	}

}
