//String 类的 indexOf() 方法在字符串中查找子字符串出现的位置，如果存在返回字符串出现的位置（第一位为0），如果不存在返回 -1
public class String_Search {
    public static void main(String[] args) {
        String strOrig = "Google Facebook Amazon";
        int intIndex = strOrig.indexOf("Facebook");
        if(intIndex == - 1){
            System.out.println("Not found  Facebook");
        }else{
            System.out.println("Facebook position in " + intIndex);
        }
    }
}
