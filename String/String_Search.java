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
