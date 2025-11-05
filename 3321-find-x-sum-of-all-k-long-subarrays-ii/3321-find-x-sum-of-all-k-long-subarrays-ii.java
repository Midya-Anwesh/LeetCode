import java.util.TreeSet;
import java.util.HashMap;
import java.util.Vector;
import java.math.BigInteger;

class Solution {
    public long[] findXSum(int[] nums, int k, int x) {
        TreeSet<int[]> maxHeap = new TreeSet<>(
            (a, b) -> (b[0] == a[0])? (b[1]-a[1]):(b[0]-a[0])
        );
        TreeSet<int[]> potentialCandidates = new TreeSet<>(
            (a, b) -> (b[0] == a[0])? (b[1]-a[1]):(b[0]-a[0])
        );
        HashMap<Integer, int[]> numFreq = new HashMap<>();
        long[] ret = new long[nums.length-k+1];

        // Maintain a running sum
        long runningSum = 0l;
        int idx = 0;
        int win_st = 0;
        // Iterate over the input
        for (int i = 0; i < nums.length; i++){
            // If current number has previously been seen
            if (numFreq.containsKey(nums[i])){
                // If it's in the heap, then remove it from the heap, update the frequency and add it back
                // Also modify running sum properly
                if (maxHeap.contains( numFreq.get(nums[i]) )){
                    runningSum -= (long) nums[i] * (numFreq.get(nums[i])[0]);
                    maxHeap.remove( numFreq.get(nums[i]) );
                }

                else if (potentialCandidates.contains( numFreq.get(nums[i]) )){
                    potentialCandidates.remove(numFreq.get(nums[i]));
                }

                int currFreq = numFreq.get(nums[i])[0];
                runningSum += (long) nums[i] * (currFreq+1);
                numFreq.put(nums[i], new int[] {currFreq+1, nums[i]});
                maxHeap.add(numFreq.get(nums[i]));
                
            }

            else {
                numFreq.put(nums[i], new int[] {1, nums[i]});
                maxHeap.add(numFreq.get(nums[i]));
                runningSum += (long) nums[i];
            }

            // Check the window length and adjust it
            // If window length is greater than k than delete the left most element
            if ((i-win_st+1) > k ){
                int[] toDel = numFreq.remove(nums[win_st++]);
                if (toDel[0] > 1){
                    if (maxHeap.contains(toDel)){
                        maxHeap.remove(toDel);
                        maxHeap.add(new int[] {toDel[0]-1, toDel[1]});
                        runningSum -= (long) nums[win_st-1];
                    }
                    if (potentialCandidates.contains(toDel)){
                        potentialCandidates.remove(toDel);
                        potentialCandidates.add(new int[] {toDel[0]-1, toDel[1]});
                    }
                    numFreq.put(toDel[1], new int[] {toDel[0]-1, toDel[1]});
                }
                else{
                    if (maxHeap.contains(toDel)){
                        maxHeap.remove(toDel);
                        runningSum -= (long) nums[win_st-1];
                    }
                    if (potentialCandidates.contains(toDel)){
                        potentialCandidates.remove(toDel);
                    }
                }

                while ( (potentialCandidates.size() >= 1) && (potentialCandidates.first()[0] >= toDel[0]-1) ){
                    int[] tup = potentialCandidates.first();
                    runningSum += (long) tup[0] * tup[1];
                    maxHeap.add(potentialCandidates.pollFirst());
                }
            }

            while (maxHeap.size() > x){
                int[] deleted = maxHeap.pollLast();
                potentialCandidates.add(deleted);
                runningSum -= (long) deleted[0] * deleted[1];
            }

            if ( (i+1) >= k){
                ret[idx++] = runningSum;
            }
        }

        if (idx <= nums.length-k){
            ret[idx++] = runningSum;
        }

        return ret;
    }
}