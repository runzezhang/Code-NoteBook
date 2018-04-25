//通过两种方式创建字符串，并测试其性能
public class String_ComparePerformance {
    public static void main(String[] args){
        long startTime = System.currentTimeMillis();
        for(int i=0;i<50000;i++){
            String s1 = "hello";
            String s2 = "hello";
        }
        long endTime = System.currentTimeMillis();
        System.out.println("keyword"
                + " : "+ (endTime - startTime)
                + " ms" );
        long startTime1 = System.currentTimeMillis();
        for(int i=0;i<50000;i++){
            String s3 = new String("hello");
            String s4 = new String("hello");
        }
        long endTime1 = System.currentTimeMillis();
        System.out.println("object"
                + " : " + (endTime1 - startTime1)
                + " ms");
    }
}
