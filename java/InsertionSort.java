//insertion sort demo

// short note about insertion sort
/*
    author: sundar rajan

    array with size 1 is already sorted.
    keep growing the size of the array , by finding the position for next element.
    Hold the new item as key, if the key is smaller to the existing arr elements keep shifting right.
    insert where the new item has to go.


*/
package cuddly_journey;
class InsertionSort {
    public static void main(String args[]) throws Exception {
        int[] arr = { 5, 6, 9, 1, 2, 3, 10, 12, 14, 7 };
        print(arr, "Before Sort");
        insertionsort(arr);
        print(arr, "Sorted");
    }

    public static void insertionsort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i;
            int key = arr[j];
            while (j > 0 && arr[j - 1] > key) {
                arr[j] = arr[j - 1];
                j = j - 1;
            }
            arr[j] = key;
        }
    }

    public static void print(int[] arr, String msg) {
        System.out.println(msg + " : ");
        for (int x : arr) {
            System.out.print(x + ", ");
        }
        System.out.print("\n");
    }

    public static void log(String msg) {
        System.out.println(msg);
    }
}
