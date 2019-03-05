package cuddly_journey;

public class LinkedList<T> {

	private int size;
	private Node<T> head;
	private Node<T> tail;

	public LinkedList() {
		size = 0;
		head = null;
		tail = null;
	}

	public void add(T obj) {
		Node<T> new_node = new Node<T>(obj);
		if (head == null) {
			head = tail = new_node;
		} else {
			tail.setNext(new_node);
			tail = tail.getNext();
		}

		size++;
	}

	public Node<T> getHead() {
		return head;
	}

	public void printAll() {
		Node<T> curr = getHead();
		System.out.println("Print Nodes :\n");
		while (curr != null) {
			System.out.printf("%d,", curr.val());
			curr = curr.getNext();
		}
		System.out.println();
	}

	public Node<T> getMid() {
		Node<T> handle1 = getHead();
		Node<T> handle2 = getHead();
		while (handle1 != null) {
			handle1 = handle1.getNext();
			if (handle1 == null)
				break;
			handle1 = handle1.getNext();
			handle2 = handle2.getNext();
		}
		return handle2;
	}

	public static void main(String args[]) throws Exception {
		// perform unit test
		LinkedList<Integer> lstInt = new LinkedList<Integer>();
		lstInt.add(5);
		lstInt.add(15);
		lstInt.add(25);
		lstInt.add(35);
		lstInt.add(50);
		lstInt.printAll();
		System.out.println("Mid : " + lstInt.getMid().val());

	}

}

class Node<T> {
	T val;
	Node<T> next;

	public Node(T obj) {
		val = obj;
		next = null;
	}

	public void setNext(Node<T> obj) {
		this.next = obj;
	}

	public Node<T> getNext() {
		return this.next;
	}

	public void setVal(T newobj) {
		this.val = newobj;
	}

	public T val() {
		return val;
	}
}
