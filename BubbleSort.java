// bubble sort demo

class BubbleSort {
    public static void main(String args[]) throws Exception {
        int[] arr = { 5, 6, 9, 1, 2, 3, 10, 12, 14, 7 };
        print(arr, "Before Sort");
        bubblesort(arr);
        print(arr, "Sorted");
    }

    public static void bubblesort(int[] arr) {
        boolean bSwapped = false;
        do {
            bSwapped = false;
            for (int i = 1; i < arr.length; i++) {
                if (arr[i - 1] > arr[i]) {
                    exchange(arr, i - 1, i);
                    bSwapped = true;
                }
            }

        } while (bSwapped);

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