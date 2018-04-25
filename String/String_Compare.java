//通过字符串函数 compareTo (string) ，compareToIgnoreCase(String) 及 compareTo(object string) 来比较两个字符串，并返回字符串中第一个字母ASCII的差值

public class String_Compare {
    public static void main(String args[]){
        String str="Hello World";
        String str2="hello world";
        Object objStr=str;

        System.out.println(str.compareTo(str2));
        System.out.println(str.compareToIgnoreCase(str2));
        System.out.println(str.compareTo(objStr.toString()));
    }

}
