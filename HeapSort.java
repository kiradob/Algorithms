public class HeapSort {
    public static void sort(int[] array) {
        // построение кучи (перегруппируем массив)
        for(int i = array.length/2-1; i >=0; i--)
            heapify(array, array.length, i);

        // поочереди извелекаем элемены из кучи
        for(int i = array.length-1; i >=0; i--) {
            // перемещаем текущий корень в конец
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;

            // вызываем heapify  на уменьшенной куче
            heapify(array, i, 0);
        }
    }

    private static void  heapify(int[] array, int heapSize, int rootIndex){
        int largest = rootIndex; // инициализация наибольшего элемента как корня
        int leftChild = 2 * rootIndex + 1;
        int rightChild = 2 * rootIndex + 2;

        // Если левый дочерний элемент больше корня
        if(leftChild < heapSize && array[leftChild] > array[largest])
            largest = leftChild;

        // Если правый дочерний элемент больще чем самый большой на данный момент элемент
        if(rightChild < heapSize && array[rightChild] > array[largest])
            largest = rightChild;

        if(largest != rootIndex){
            int temp = array[rootIndex];
            array[rootIndex] = array[largest];
            array[largest] = temp;

            // рекурсивно преобразуем в двоичную кучу затронутое дерево
            heapify(array, heapSize, largest);
        }
    }

}