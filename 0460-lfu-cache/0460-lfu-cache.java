class LFUCache {
    int maxSize, size, time; 
    Comparator<int[]> arrayComparator;
    TreeSet<int[]> callTree;
    HashMap<Integer, int[]> callMap;

    public LFUCache(int capacity) {
        this.maxSize = capacity;
        this.size = 0;
        this.time = 0;
        this.arrayComparator = new Comparator<int[]>() {
            @Override
            public int compare(int[] arr1, int[] arr2) {
                 // Ensure arrays are of length 3 before comparing
                if (arr1.length != 3 || arr2.length != 3) {
                    throw new IllegalArgumentException("Arrays must be of length 3");
                }

                // Compare elements lexicographically
                for (int i = 0; i < 3; i++) {
                    int comparison = Integer.compare(arr1[i], arr2[i]);
                    if (comparison != 0) {
                        return comparison;
                    }
                }
                // If all elements are equal, the arrays are considered equal
                return 0;
            }
        };

        // Create a TreeSet with the custom Comparator
        this.callTree = new TreeSet<>(arrayComparator); // Stores [freq, addTime, key]
        this.callMap = new HashMap<>(); // Maps key -> [value, addTime, frequency]
    }
    
    public int get(int key) {
        if (this.callMap.containsKey(key)){
            this.time += 1;
            int []callInfo = this.callMap.get(key);
            int value = callInfo[0], addTime = callInfo[1], freq = callInfo[2];
            this.callTree.remove(new int[]{freq, addTime, key});
            this.callTree.add(new int[]{freq+1, this.time, key});
            callInfo[1] = this.time;
            callInfo[2] = freq+1;
            this.callMap.put(key, callInfo);
            return value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (this.size >= this.maxSize){
            if (this.size == 0){
                return;
            }
            int []toDel = this.callTree.pollFirst();
            this.callMap.remove(toDel[2]);
            this.size -= 1;
        }
        this.time += 1;
        int []callInfo = {value, this.time, 1};
        this.callTree.add(new int[]{1, this.time, key});
        this.callMap.put(key, callInfo);
        this.size += 1;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */