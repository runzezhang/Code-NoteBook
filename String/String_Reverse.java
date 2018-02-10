public class String_Reverse {
    public static void main(String[] args){
        String string="runzezhang";
        String reverse = new StringBuffer(string).reverse().toString();
        System.out.println("Before:"+string);
        System.out.println("After:"+reverse);
    }
}
