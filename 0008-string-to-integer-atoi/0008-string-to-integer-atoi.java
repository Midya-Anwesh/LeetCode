class Solution {
    public int myAtoi(String s) {
        if (s.length() == 0){
            return 0;
        }
        long res = 0;
        boolean negetive = false;
        short index = 0;

        for (; index < s.length(); index++){
            if (s.charAt(index)!=' '){
                break;
            }
            else if(index == s.length()-1){
                return 0;
            }
        }
        if (s.charAt(index)=='-'){
            negetive = true;
            index++;
        }
        else if (s.charAt(index)=='+'){
            index++;
        }

        for (; index < s.length(); index++){
            if (!Character.isDigit(s.charAt(index))){
                break;
            }
            res = (res*10)+(s.charAt(index)-48);
            if ( (negetive && ( (-1*res) <= Integer.MIN_VALUE ) ) ){
                return Integer.MIN_VALUE;
            }
            else if ( (!negetive) && (res >= Integer.MAX_VALUE)){
                return Integer.MAX_VALUE;
            }
        }
        if (negetive){
            res = -1*res;
        }
        return (int)res;
    }
}