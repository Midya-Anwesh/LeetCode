import java.util.TreeSet;
import java.util.HashMap;
import java.util.Vector;
import java.util.stream.IntStream;

class Solution {
    int getParent(int vertex, int[] parent){
        if (parent[vertex] == vertex){
            return vertex;
        }
        int p = getParent(parent[vertex], parent);
        parent[vertex] = p;
        return p;
    }
    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        int []parent = new int[c];
        int []rank = new int[c];
        HashMap<Integer, TreeSet<Integer>> childs = new HashMap<>();
        HashMap<Integer, Integer> isOnline = new HashMap<>();

        for (int i = 0; i < c; i++){
            parent[i] = i;
        }
        for (int i = 0; i < connections.length; i++){
            int Uparent1 = getParent(connections[i][0]-1, parent);
            int Uparent2 = getParent(connections[i][1]-1, parent);

            if (rank[Uparent1] >= rank[Uparent2]){
                parent[Uparent2] = Uparent1;
                rank[Uparent1] += 1;
            }
            else {
                parent[Uparent1] = Uparent2;
                rank[Uparent2] += 1;
            }
        }
        for (int i = 0; i < c; i++){
            isOnline.put(i, 1); // 1 signifies the station is online
            int Uparent = getParent(i, parent); // Get the Ultimate Parent of the station, and add it to the treemap of the ultimate parent
            if (!childs.containsKey(Uparent)){
                childs.put(Uparent, new TreeSet<Integer>());
            }
            childs.get(Uparent).add(i);
        }

        Vector<Integer> ret = new Vector<>();
        for (int i = 0; i < queries.length; i++){
            if (queries[i][0] == 1){
                if (isOnline.get(queries[i][1]-1) == 1){
                    ret.add(queries[i][1]);
                }
                else {
                    int Uparent = getParent(queries[i][1]-1, parent);
                    if (childs.get(Uparent).isEmpty()){
                        ret.add(-1);
                    }
                    else{
                        ret.add(childs.get(Uparent).first()+1);
                    }
                }
            }
            else {
                if (isOnline.get(queries[i][1]-1) == 1){
                    int Uparent = getParent(queries[i][1]-1, parent);
                    isOnline.put(queries[i][1]-1, 0);
                    childs.get(Uparent).remove(queries[i][1]-1);
                }
            }
        }
        
        int []ans = new int[ret.size()];
        for (int i = 0; i < ret.size(); i++){
            ans[i] = ret.get(i);
        }
        return ans;
    }
}