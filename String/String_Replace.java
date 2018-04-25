//替换字符串中的字符

public class String_Replace {
    public static void main(String args[]){
        String str="Hello World";
        System.out.println( str.replace( 'H','W' ) );
        System.out.println( str.replaceFirst("He", "Wa") );
        System.out.println( str.replaceAll("He", "Ha") );
    }
}
