public class SelectionSort{

	public static void main(String args[]){

		int arr[] = {64,25,12,22,11};

		for (int i=0; i<arr.length;i++) {

			int min = i;
			
			for (int j=i; j<arr.length; j++) {

				if (arr[j] < arr[min]) {
					min = j;
				}
			}

			swap(arr,i,min);

		}

		for (int x:arr) {
			System.out.print(x + " ");
		}	
	}

	private static void swap (int[] arr, int src, int target) {
		int temp = arr[src];
		arr[src] = arr[target];
		arr[target] = temp;
	}
}






