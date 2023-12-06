public class Main {
    static void printArray(int[] array)
    {
        for (int j : array) System.out.print(j + " ");
        System.out.println();
    }

    // Управляющая программа
    public static void main(String[] args)
    {
        int[] array = {112, 141, 13, 52, 6, 71};
        HeapSort.sort(array);

        System.out.println("Sorted array is");
        printArray(array);
    }
}