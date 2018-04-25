import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
//通过 List 类的 Arrays.toString () 方法和 List 类的 list.Addall(array1.asList(array2) 方法将两个数组合并为一个数组
public class Array_Merge {
    public static void main(String args[]) {
        String a[] = { "A", "E", "I" };
        String b[] = { "O", "U" };
        List list = new ArrayList(Arrays.asList(a));
//        List是一个接口，而ListArray是一个类。
//        ListArray继承并实现了List。
//        所以List不能被构造，但可以向上面那样为List创建一个引用，而ListArray就可以被构造。
//        List list;     //正确   list=null;
//        List list=new List();    //   是错误的用法
//        List list = new ArrayList();这句创建了一个ArrayList的对象后把上溯到了List。此时它是一个List对象了，有些ArrayList有但是List没有的属性和方法，它就不能再用了。
//        而ArrayList list=new ArrayList();创建一对象则保留了ArrayList的所有属性。
        list.addAll(Arrays.asList(b));
        Object[] c = list.toArray();
        System.out.println(Arrays.toString(c));
    }
}
