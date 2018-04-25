//使用 StringTokennizer 设置不同分隔符来分隔字符串，默认的分隔符是：空格、制表符（\t）、换行符(\n）、回车符（\r）

import java.util.StringTokenizer;

public class String_Tokenizer {
    public static void main(String[] args) {

        String str = "This is String , split by StringTokenizer, created by runze";
        StringTokenizer st = new StringTokenizer(str);

        System.out.println("----- space ------");
        while (st.hasMoreElements()) {
            System.out.println(st.nextElement());
        }

        System.out.println("----- comma ------");
        StringTokenizer st2 = new StringTokenizer(str, ",");

        while (st2.hasMoreElements()) {
            System.out.println(st2.nextElement());
        }
    }
}
