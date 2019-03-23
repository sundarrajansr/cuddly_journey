package cuddly_journey;

import java.util.NoSuchElementException;

/*
 * change log
 * -------------------------------
 * 18-Mar-2019 Initial implementation
 * 23-Mar-2019 bst operations - insert, find, height
 * 
 * -------------------------------
 */
/*
 * todo
 * 
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
					new_node.setParent(parent);
					return this;
				}
			} else if (compare > 0) {
				cnode = cnode.right();
				if (cnode == null) {
					parent.setRight(new_node);
					new_node.setParent(parent);
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
		System.out.printf("Node : %s, Left : %s, Right : %s Parent : %s\n", node.val(),
				node.left() == null ? "null" : node.left().val(), node.right() == null ? "null" : node.right().val(),
				node.parent() == null ? "null" : node.parent().val());
		if (node.left() != null)
			printAllNodes(node.left());
		if (node.right() != null)
			printAllNodes(node.right());

	}

	public Node<Q> find(Q val) {

		Node<Q> pointer = root;
		while (pointer != null) {
			int diff = pointer.val().compareTo(val);
			if (diff == 0) {
				return pointer;
			} else if (diff < 0) {
				pointer = pointer.right();
			} else {
				pointer = pointer.left();
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

		height = heightUtil(root);
		return height;

	}

	private int heightUtil(Node<Q> node) {
		if (node == null)
			return -1;
		else
			return (1 + Math.max(heightUtil(node.left()), heightUtil(node.right())));

	}

	public Node<Q> maximum(Node<Q> q) {
		while (q.right() != null) {
			q = q.right();
		}
		return q;
	}

	public Node<Q> minimum(Node<Q> q) {
		while (q.left() != null) {
			q = q.left();
		}
		return q;
	}

	public Node<Q> successor(Q val) {
		Node<Q> curnode = this.find(val);
		if (curnode == null)
			throw new NoSuchElementException();
		if (curnode.right() != null) {
			return (minimum(curnode.right()));
		} else {
			Node<Q> p = curnode.parent();
			while (p != null && p == curnode.right()) {
				curnode = p;
				p = p.parent();
			}
			return p;
		}
	}

	public Node<Q> predecessor(Q val) {
		Node<Q> curnode = this.find(val);
		if (curnode == null)
			throw new NoSuchElementException();
		if (curnode.left() != null) {
			return (maximum(curnode.left()));
		} else {
			Node<Q> p = curnode.parent();
			while (p != null && p == curnode.left()) {
				curnode = p;
				p = p.parent();
			}
			return p;
		}
	}

	public void delete(Q val) {

		Node<Q> del_node = this.find(val);
		if (del_node == null)
			throw new NoSuchElementException();

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

		public String toString() {
			return "Node : " + val.toString();
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
	public static void main(String[] args) throws Exception {

		BinarySearchTree<Integer> bst = new BinarySearchTree<Integer>();

		bst.insert(5).insert(3).insert(2).insert(1).insert(4).insert(10).insert(15).insert(12).insert(14);
		bst.print();

		System.out.println(bst.find(3));
		System.out.println(bst.find(22));
		System.out.println(bst.find(12));
		System.out.println("width" + bst.width());
		System.out.println("height" + bst.height());
		System.out.println("pred of 5 is "+ bst.predecessor(5));
		System.out.println("pred of 12 is "+ bst.predecessor(12));
		System.out.println("suc of 3 is "+bst.successor(3));
		System.out.println("suc of 14 is "+bst.successor(14));
		System.out.println("suc of 15 is "+bst.successor(15));
	}

}
