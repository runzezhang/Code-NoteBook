//By Runze Zhang
class Solution {
    public boolean isPalindrome(int x) {
        //transfer negative number
        if(x<0)
            return false;
        if(x==0)
            return true;
        if(x>2147483647)
            return false;
            // caculate number size
        int intsize=0;
        Integer[] size={9,99,999,9999,99999,999999,9999999,99999999,999999999,2147483647};
        for(int j=0;j<size.length;j++){
            if(x<=size[j]){
                    intsize=j+1;
                    break;
                }
            }
        if(intsize==1){
            return true;
        }
        int[] xarray=new int[intsize];
        for(int k=0;k<intsize;k++){
            xarray[k]=x%10;
            x=x/10;
        }
        boolean judge=true;
        for(int l=0;l<(intsize/2);l++){
            if(xarray[l]!=xarray[intsize-1-l]){
                judge=false;
                break;
            }
        }
        return judge;        
    }
}