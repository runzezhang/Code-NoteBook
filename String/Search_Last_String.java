//通过字符串函数 strOrig.lastIndexOf(Stringname) 来查找子字符串 Stringname 在 strOrig 出现的位置

public class Search_Last_String {
    public static void main(String[] args) {
        String strOrig = "Hello world ,Hello Runze";
        int lastIndex = strOrig.lastIndexOf("Runze");
        if(lastIndex == - 1){
            System.out.println("Not found Runze");
        }else{
            System.out.println("Runze last found position： "+ lastIndex);
        }
    }
}
