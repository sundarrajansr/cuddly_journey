//Quick sort demo java
package cuddly_journey;
class QuickSort {
    public static void main(String args[]) throws Exception {
        int[] arr = { 5, 6, 9, 1, 2, 3, 10, 12, 14, 7 };
        print(arr, "Before Sort");
        quicksort(arr, 0, arr.length - 1);
        print(arr, "Sorted");
    }

    public static void quicksort(int[] arr, int p, int r) {
        log("QuickSort [ " + p + ", " + r + "]");
        if (p < r) {
            int q = partition(arr, p, r);
            quicksort(arr, p, q - 1);
            quicksort(arr, q + 1, r);
        }
    }

    private static int partition(int[] arr, int p, int r) {
        log("partition [ " + p + ", " + r + "]");
        int key = arr[r];
        int i = p - 1;
        for (int j = p; j < r; j++) {
            if (arr[j] <= key) {
                i = i + 1;
                exchange(arr, j, i);
            }
        }
        exchange(arr, i + 1, r);
        return (i + 1);
    }

    private static void exchange(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
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