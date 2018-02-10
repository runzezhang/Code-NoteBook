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
