//By Runze Zhang
class Solution {
    public int reverse(int x) {
        int bitp=2147483647;
        int bitn=-2147483648;
        // for(int i=1;i<33;i++){
        //     bit=bit*2;
        // }
        //transfer negative number
        int p=0;
        int positive=1;
        if(x<0){
            p=-x;
            positive=-1;
        }else{p=x;}
        // caculate number size
        int intsize=0;
        Integer[] size={9,99,999,9999,99999,999999,9999999,99999999,999999999,2147483647};
        for(int j=0;j<size.length;j++){
            if(p<=size[j]){
                if(p!=0){
                    intsize=j+1;
                    break;
                }
            }
        }
        Integer[] shape={2,1,4,7,4,8,3,6,4,7};
        
        int[] xarray=new int[intsize];
        for(int k=0;k<intsize;k++){
            xarray[k]=p%10;
            p=p/10;
        }
        

        // reverse
        int temp=0;
        for(int l=0;l<(intsize/2);l++){
            temp=xarray[l];
            xarray[l]=xarray[intsize-1-l];
            xarray[intsize-1-l]=temp;
        }
        

        // change reverse array to int
        int y=0;
        int power=1;
        for(int m=0;m<intsize;m++){
            y=y+xarray[m]*power;
            power=power*10;
        }
        //
        if(intsize==10){
            for(int n=0;n<intsize;n++){
                if(xarray[intsize-1-n]>shape[n]){
                    y=0;
                    break;
                }else if(xarray[intsize-1-n]<shape[n]){
                    break;
                }
            }
        }
        // return part
        if(x==-2147483648){
            return 0;
        }
        else{
            
            return y*positive;
            // return xarray[0];
        }
    }
}