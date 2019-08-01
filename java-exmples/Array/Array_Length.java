//使用数组的属性 length 来获取数组的长度

public class Array_Length {
    public static void main(String args[]) {
        String[][] data = new String[2][5];
        System.out.println("第一维数组长度: " + data.length);
        System.out.println("第二维数组长度: " + data[0].length);
    }
}
