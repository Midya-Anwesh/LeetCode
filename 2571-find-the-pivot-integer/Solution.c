// runtime = 3.0ms
// memory usage = 5.5MB

int pivotInteger(int n) {
    int pivot = ((n+1)/2) + (int)(floor(sqrt(n)));
        int left_sum = (pivot*(pivot+1))/2;
            int right_sum = ((n*(n+1))/2) - left_sum + pivot;
                
                    if(left_sum > right_sum){
                            while(left_sum > right_sum){
                                        left_sum -= pivot;
                                                    pivot -= 1;
                                                                right_sum += pivot;
                                                                        }
                                                                            }
                                                                                else if(left_sum < right_sum){
                                                                                        while(left_sum < right_sum){
                                                                                                    right_sum -= pivot;
                                                                                                                pivot += 1;
                                                                                                                            left_sum += pivot;
                                                                                                                                    }
                                                                                                                                        }
                                                                                                                                            
                                                                                                                                                if(left_sum == right_sum){
                                                                                                                                                        return pivot;
                                                                                                                                                            }
                                                                                                                                                                
                                                                                                                                                                    return -1;
}