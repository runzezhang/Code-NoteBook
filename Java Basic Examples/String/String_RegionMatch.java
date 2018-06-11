//使用了 regionMatches() 方法测试两个字符串区域是否相等
public class String_RegionMatch {
    public static void main(String[] args){
        String first_str = "Welcome to Google";
        String second_str = "I work with Google";
        boolean match1 = first_str.
                regionMatches(11, second_str, 12, 9);
        boolean match2 = first_str.
                regionMatches(true, 11, second_str, 12, 9); //第一个参数 true 表示忽略大小写区别
        System.out.println("Care Upper：" + match1);
        System.out.println("Don't care Upper：" + match2);
    }
}
