//split(string) 方法通过指定分隔符将字符串分割为数组
public class String_Split {
    public static void main(String args[]){

        String str = "www-runzezhang-com";
        String[] temp;
        String delimeter = "-";  // 指定分割字符
        temp = str.split(delimeter); // 分割字符串
        // 普通 for 循环
        for(int i =0; i < temp.length ; i++){
            System.out.println(temp[i]);
            System.out.println("");
        }

        System.out.println("------java for each-----");
        String str1 = "www.runzezhang.com";
        String[] temp1;
        String delimeter1 = "\\.";  // 指定分割字符， . 号需要转义
        temp1 = str1.split(delimeter1); // 分割字符串
        for(String x :  temp1){
            System.out.println(x);
            System.out.println("");
        }
    }
}
