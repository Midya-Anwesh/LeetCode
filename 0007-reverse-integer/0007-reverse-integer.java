class Solution {
    public int reverse(int x) {
        System.out.println(x);
        long res = 0;
        int negetive = (x < 0)? 1:0;
        x = Math.abs(x);
        while (x > 0){
            res = (res*10)+(x%10);
            x /= 10;
        }
        if (res > Integer.MAX_VALUE){
            return 0;
        }
        res = (negetive==1)? res*-1:res;
        return (int)res;
    }
}