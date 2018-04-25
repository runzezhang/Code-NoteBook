//import java.util.Arrays;使用sort()方法对Java数组进行排序，及如何使用 binarySearch() 方法来查找数组中的元素, 这边我们定义了 printArray() 方法来打印数组

import java.util.Arrays;

public class Array_SearchSort {
    public static void main(String args[]) throws Exception {
        int array[] = { 2, 5, -2, 6, -3, 8, 0, -7, -9, 4 };
        Arrays.sort(array);
        printArray("sort array: ", array);
        int index = Arrays.binarySearch(array, 2);
        System.out.println(" 2  is on  " + index + " location");
    }
    private static void printArray(String message, int array[]) {
        System.out.println(message
                + ": [length: " + array.length + "]");
        for (int i = 0; i < array.length; i++) {
            if(i != 0){
                System.out.print(", ");
            }
            System.out.print(array[i]);
        }
        System.out.println();
    }

}
