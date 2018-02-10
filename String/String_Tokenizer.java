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
