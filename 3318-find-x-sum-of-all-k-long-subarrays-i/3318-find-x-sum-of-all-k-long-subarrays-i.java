import java.util.TreeSet;
import java.util.HashMap;
import java.util.Vector;
import java.math.BigInteger;

class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        TreeSet<int[]> maxHeap = new TreeSet<>(
            (a, b) -> (b[0] == a[0])? (b[1]-a[1]):(b[0]-a[0])
        );
        TreeSet<int[]> potentialCandidates = new TreeSet<>(
            (a, b) -> (b[0] == a[0])? (b[1]-a[1]):(b[0]-a[0])
        );
        HashMap<Integer, int[]> numFreq = new HashMap<>();
        int[] ret = new int[nums.length-k+1];

        // Maintain a running sum
        int runningSum = 0;
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
                runningSum += nums[i] * (currFreq+1);
                numFreq.put(nums[i], new int[] {currFreq+1, nums[i]});
                maxHeap.add(numFreq.get(nums[i]));
                
            }

            else {
                numFreq.put(nums[i], new int[] {1, nums[i]});
                maxHeap.add(numFreq.get(nums[i]));
                runningSum += nums[i];
            }

            // Check the window length and adjust it
            // If window length is greater than k than delete the left most element
            if ((i-win_st+1) > k ){
                int[] toDel = numFreq.remove(nums[win_st++]);
                if (maxHeap.contains(toDel)){
                    maxHeap.remove(toDel);
                    runningSum -= toDel[0] * toDel[1];
                }
                if (potentialCandidates.contains(toDel)){
                    potentialCandidates.remove(toDel);
                }
                if (toDel[0] >= 1){
                    numFreq.put(toDel[1], new int[]{toDel[0]-1, toDel[1]});
                    potentialCandidates.add(numFreq.get(toDel[1]));
                }

                while ( (potentialCandidates.size() >= 1) && (maxHeap.size() < x) ){
                    int []tup = potentialCandidates.pollFirst();
                    maxHeap.add(tup);
                    runningSum += tup[0] * tup[1];
                }

            }

            while (maxHeap.size() > x){
                int[] deleted = maxHeap.pollLast();
                potentialCandidates.add(deleted);
                runningSum -= deleted[0] * deleted[1];
            }

            if ( (potentialCandidates.size() >= 1) && (potentialCandidates.size() >= 1) ){
                int []bestCandidate = potentialCandidates.first();
                int []worst = maxHeap.last();
                if ( (bestCandidate[0] > worst[0]) || ( (bestCandidate[0] == worst[0]) && (bestCandidate[1] > worst[1]) ) ){
                    potentialCandidates.pollFirst();
                    maxHeap.remove(worst);
                    runningSum -= worst[0] * worst[1];
                    runningSum += bestCandidate[0] * bestCandidate[1];
                    maxHeap.add(bestCandidate);
                    potentialCandidates.add(worst);
                }
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