void quicksort(int arr[], int low, int high) {
    int i = low, j = high, pivot = arr[(low + high) / 2];
    while (i <= j) {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i <= j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
    if (low < j)
        quicksort(arr, low, j);
    if (i < high)
        quicksort(arr, i, high);
}
