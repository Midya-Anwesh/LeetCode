class Solution {
    public int reverse(int x) {
        System.out.println(x);
        int res = 0, negetive = (x < 0)? 1:0;
        x = Math.abs(x);
        while (x > 0){
            if (res > Integer.MAX_VALUE/10){
                return 0;
            }
            res = (res*10)+(x%10);
            x /= 10;
        }
        res = (negetive==1)? res*-1:res;
        return res;
    }
}